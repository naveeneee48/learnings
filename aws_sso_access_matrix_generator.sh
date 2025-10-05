#!/bin/bash
set -e
#this shell script is Automating IAM Identity Center (AWS SSO) Access Matrix Generator that fetches who has access to what account and permission set — and delivers it as a colorful Excel file 💼📊

# ====== INPUT VARIABLES ======
IDENTITY_STORE_ID="<identity_store_id>"   # Replace with your Identity Store ID
INSTANCE_ARN="arn:aws:sso:::instance/ssoins-<instance_arn>"   # Replace with your SSO Instance ARN from vanna-health account
REGION="us-east-1"

# Timestamped file names
timestamp=$(date +"%b_%d_%H_%M")   # Example: Oct_05_14_30
CSV_FILE="AWS_Access_Matrix_${timestamp}.csv"
XLSX_FILE="AWS_Access_Matrix_${timestamp}.xlsx"
# =============================

TMP_USERS="users_map.txt"
TMP_DATA="access_raw.txt"
ACC_FILE="accounts.txt"
ACC_NAMES="account_names.txt"
PERM_FILE="permission_names.txt"

: > "$TMP_USERS"
: > "$TMP_DATA"

echo "Fetching Identity Center user and access details...⏳"

# 1) Get all users (UserId + Email)
aws identitystore list-users \
  --identity-store-id "$IDENTITY_STORE_ID" \
  --region "$REGION" \
  --query 'Users[*].[UserId,Emails[0].Value]' \
  --output text > "$TMP_USERS"

# 2) Get all accounts safely (handles spaces in names)
aws organizations list-accounts --output json \
  | jq -r '.Accounts[] | "\(.Id)|\(.Name)"' > "$ACC_FILE"

# Derive just the account names (one per line, preserving spaces)
cut -d"|" -f2 "$ACC_FILE" > "$ACC_NAMES"

# 3) Get all PermissionSet ARNs
permission_sets=$(aws sso-admin list-permission-sets \
  --instance-arn "$INSTANCE_ARN" \
  --region "$REGION" \
  --query 'PermissionSets[*]' \
  --output text)

# 4) Build mapping data: write tab-separated lines: PermissionSet<TAB>AccountName<TAB>Email
while IFS="|" read -r account_id account_name; do
  echo "🔍 Processing account: $account_name ($account_id)..."
  for permarn in $permission_sets; do
    perm_name=$(aws sso-admin describe-permission-set \
      --instance-arn "$INSTANCE_ARN" \
      --permission-set-arn "$permarn" \
      --region "$REGION" \
      --query 'PermissionSet.Name' \
      --output text)

    assignments=$(aws sso-admin list-account-assignments \
      --instance-arn "$INSTANCE_ARN" \
      --account-id "$account_id" \
      --permission-set-arn "$permarn" \
      --region "$REGION" \
      --query 'AccountAssignments[*].[PrincipalId]' \
      --output text)

    for principal in $assignments; do
      # TMP_USERS is tab-delimited "UserId <TAB> Email"
      email=$(grep -w "$principal" "$TMP_USERS" | awk '{print $2}')
      if [ -n "$email" ]; then
        printf "%s\t%s\t%s\n" "$perm_name" "$account_name" "$email" >> "$TMP_DATA"
      fi
    done
  done
done < "$ACC_FILE"

echo "✅ Mapping collected. Building matrix CSV..."

# 5) Build CSV Matrix (one row per PermissionSetName, one column per Account Name)
cut -f1 "$TMP_DATA" | sort -u > "$PERM_FILE"

# Header
printf "PermissionSetName" > "$CSV_FILE"
while IFS= read -r acc; do
  printf ",%s" "$acc" >> "$CSV_FILE"
done < "$ACC_NAMES"
printf "\n" >> "$CSV_FILE"

# Rows
while IFS= read -r perm; do
  # Quote the permission set (may have spaces)
  row="\"$perm\""

  while IFS= read -r acc; do
    # Select emails where (perm, acc) matches; TMP_DATA is tab-separated
    emails=$(awk -F '\t' -v p="$perm" -v a="$acc" '$1==p && $2==a {print $3}' "$TMP_DATA" | sort -u)
    if [ -z "$emails" ]; then
      row="${row},\"\""
    else
      # Put each email on its own line inside the CSV cell; later converted to Excel real newlines
      cell=$(echo "$emails" | tr '\n' '\r')
      row="${row},\"$cell\""
    fi
  done < "$ACC_NAMES"

  echo "$row" >> "$CSV_FILE"
done < "$PERM_FILE"

# Clean intermediate text files (keep only the CSV)
rm -f "$TMP_USERS" "$TMP_DATA" "$ACC_FILE" "$ACC_NAMES" "$PERM_FILE"

# 6) Setup Python environment
echo "Setting up Python environment...🐍"
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
# shellcheck disable=SC1091
source venv/bin/activate
pip install -q pandas openpyxl

# 7) Convert CSV → Excel with styling, borders, and line breaks
echo "Creating styled Excel file...🎨"

python3 << 'PYCODE'
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows

import glob, os

# Use the newest CSV that matches the pattern
csv_files = sorted(glob.glob("AWS_Access_Matrix_*.csv"), key=os.path.getmtime, reverse=True)
csv_file = csv_files[0]
xlsx_file = csv_file.replace(".csv", ".xlsx")

df = pd.read_csv(csv_file, dtype=str).fillna("")

wb = Workbook()
ws = wb.active
ws.title = "AWS Access Matrix"

for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)

# Styling
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(color="FFFFFF", bold=True)
thin_border = Border(
    left=Side(style="thin", color="D3D3D3"),
    right=Side(style="thin", color="D3D3D3"),
    top=Side(style="thin", color="D3D3D3"),
    bottom=Side(style="thin", color="D3D3D3")
)

# Header styling
for cell in ws[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = thin_border

# Body cells
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.border = thin_border
        if cell.column == 1:
            cell.font = Font(bold=True, color="2E75B6")
            cell.fill = PatternFill(start_color="E8EEF7", end_color="E8EEF7", fill_type="solid")
        else:
            cell.fill = PatternFill(start_color="F2F6FA", end_color="F2F6FA", fill_type="solid")
            if isinstance(cell.value, str):
                # Convert the placeholder \r into real line breaks
                cell.value = cell.value.replace("\\r", "\n")

# Freeze header row
ws.freeze_panes = "A2"

# Auto column width
for col in ws.columns:
    max_len = max(len(str(c.value)) if c.value else 0 for c in col)
    ws.column_dimensions[col[0].column_letter].width = min(max_len + 5, 50)

wb.save(xlsx_file)
print(f"✅ Excel file saved: {xlsx_file}")
PYCODE

deactivate
echo "🎉 Done! File generated: $XLSX_FILE"
