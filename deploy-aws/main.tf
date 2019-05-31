provider "aws" {
  region = "${var.aws_region}"
}

data "aws_availability_zones" "available" {}

// Get My Public IP To access to database
data "http" "mypublicip" {
  url = "http://ipv4.icanhazip.com"
}

// Create VPC
// Module Source: https://github.com/terraform-aws-modules/terraform-aws-vpc
module "vpc" {
  source               = "terraform-aws-modules/vpc/aws"
  name                 = "${var.api_name}-${var.env}-vpc"
  cidr                 = "${var.vpc_cidr}"
  public_subnets       = "${var.public_subnets}"
  azs                  = ["${data.aws_availability_zones.available.names[0]}"]
  enable_dns_hostnames = true
  enable_dns_support   = true
  instance_tenancy     = "default"
  tags = {
    Terraform   = "true"
    Environment = "${var.env}"
  }
}


data "aws_ami" "ubuntu" {
  most_recent = true
  owners = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

data "local_file" "public_key" {
  filename = "key.pub"
}


resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = "${data.local_file.public_key.content}"
}

resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow ssh inbound traffic"
  vpc_id      = "${module.vpc.vpc_id}"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["${chomp(data.http.mypublicip.body)}/32"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
}


resource "aws_instance" "instance" {
  ami             = "${data.aws_ami.ubuntu.id}"
  instance_type   = "t2.micro"
  subnet_id       = "${module.vpc.public_subnets[0]}"
  key_name        = "${aws_key_pair.deployer.key_name}"
  security_groups = ["${aws_security_group.allow_ssh.id}"]
}