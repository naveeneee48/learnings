terraform {
  backend "s3" {
    bucket = "naveeneee48-s3-bucket1"
    region = "us-west-2"
    key = "naveeneee48-terraform.tfstate"
    dynamodb_table = "terraform-lock"
  }
}