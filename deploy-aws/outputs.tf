output "InstancePublicIP" {
  description = "Instance Public IP"
  value       = "${aws_instance.instance.public_ip}"
}
