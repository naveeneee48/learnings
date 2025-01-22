provider "aws" {
  region = "us-west-2" # Set your desired AWS region
}

resource "aws_instance" "my-server" {
  ami           = var.ami_value # Specify an appropriate AMI ID
  instance_type = var.instance_type_value
  key_name      = var.key_value_pair
  tags = {
    Name = var.tag_for_instance
  }
}
