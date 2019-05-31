# Deploy

## Docker

**Requirements**

- Docker

```bash
git clone https://github.com/fdmsantos/moving-average
cd moving-average/
make build-docker
docker run --rm -v $(pwd)/data:/data moving_average -i /data/events.json -w 10
```

### Without make

```bash
git clone https://github.com/fdmsantos/moving-average
cd moving-average/
docker build -t moving_average .
docker run --rm -v $(pwd)/data:/data moving_average -i /data/events.json -w 10
```

## AWS

**Requirements**

- AWS Cli with proper login configured

```bash
# Run following command to test it
aws s3 ls
```

- Terraform - version 0.12

```bash
# Run following command to test it
terraform -version
```

- Ansible

```bash
# Run following command to test it
ansible --version
```

**Deploy**

```bash
git clone https://github.com/fdmsantos/moving-average
cd moving-average/
make build-aws
```

**Deploy Without make**

```bash
git clone https://github.com/fdmsantos/moving-average
cd moving-average/deploy-aws
# Generate SSH Keys
ssh-keygen -t rsa -b 4096 -N "" -f $(pwd)/key

# Deploy AWS Infra
terraform init
terraform apply

# Configure EC2 Instance and Deploy moving average app on EC2 Instance
ansible-playbook -u ubuntu --key-file key -i $(terraform output InstancePublicIP), deploy.yml
```

**Test**

```bash

# path : moving-average/deploy-aws
ssh -i key ubuntu@$(terraform output InstancePublicIP)
cd /app
docker run --rm -v $(pwd)/data:/data moving_average -i /data/events.json -w 10
```


**Destroy**

```bash
make destroy-aws
# or (path: moving-average/deploy-aws)
terraform destroy
rm key key.pub
```

# Run Tests

```bash
git clone https://github.com/fdmsantos/moving-average
cd moving-average/
python test_calculate_cli.py
# Or
make run-tests
```