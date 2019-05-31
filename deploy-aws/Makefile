.PHONY: build-terraform create-ssh-keys ansible
create-ssh-keys:
	ssh-keygen -t rsa -b 4096 -f ${CURDIR}/key -N ""

build-terraform:
	terraform init
	TF_CLI_ARGS_apply="-auto-approve" terraform apply

destroy-terraform:
	terr

ansible:
	ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook -u ubuntu --key-file key -i $$(terraform output InstancePublicIP), deploy.yml

build-aws: create-ssh-keys build-terraform ansible

destroy-aws:
	rm key key.pub
	TF_CLI_ARGS_apply="-auto-approve" terraform destroy