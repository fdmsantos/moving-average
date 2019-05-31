.PHONY: build-terraform create-ssh-keys ansible destroy-terraform delete-ssh-keys wait

ssh_keys_dir = ${CURDIR}/deploy-aws
remote_ssh_user = ubuntu

create-ssh-keys:
	ssh-keygen -t rsa -b 4096 -f $(ssh_keys_dir)/key -N ""

delete-ssh-keys:
	rm $(ssh_keys_dir)/key $(ssh_keys_dir)/key.pub

build-terraform:
	cd deploy-aws; terraform init; terraform apply -auto-approve

destroy-terraform:
	cd deploy-aws; terraform destroy -auto-approve

ansible:
	cd deploy-aws; ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook -u $(remote_ssh_user) --key-file key -i $$(terraform output InstancePublicIP), deploy.yml

build-docker:
	docker build -t moving_average .

run-tests:
	python test_calculate_cli.py

wait:
	sleep 20

build-aws: create-ssh-keys build-terraform wait ansible

destroy-aws: destroy-terraform delete-ssh-keys
