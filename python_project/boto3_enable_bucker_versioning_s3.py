import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Enable versioning
bucket_name = 'my-bucket-name'
response = s3.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={
        'Status': 'Enabled'
    }
)

print(f"Versioning enabled for bucket: {bucket_name}")
