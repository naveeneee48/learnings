provider "aws" {
  region = "us-west-2"
}

module "ec2_instance" {
  source              = "./module/ec2_instances"
  ami_value           = "ami-055e3d4f0bbeb5878"
  instance_type_value = "t2.micro"
  tag_for_instance    = "naveen-server"
  key_value_pair      = "cyberblitz-attack"
}