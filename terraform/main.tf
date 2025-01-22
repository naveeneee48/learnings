provider "aws" {
  region =  "us-west-2"
}
resource "aws_instance" "naveen-server" {
            instance_type = "t2.micro"
            ami = "dwsvdfvsdf"
            tags = {
              Names = "naveen-server3"
            }
}

