variable "aws_region" {
  default = "eu-west-1"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "public_subnets" {
  type    = "list"
  default = [ "10.0.0.0/20" ]
}

variable "env" {
  default = "dev"
}

variable "api_name" {
  default = "moving-average"
}