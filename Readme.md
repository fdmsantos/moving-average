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

# Extend Moving Average App

You are welcome to improve/add new features.
Please read this section before starts write new code

## Add new Input Type

The moving average app uses Strategy Design Pattern to add new input type.
If you want add new input type like csv, yaml, xml, ... you need do the follow.
**Example**: Lets add csv input type

1. Create a file (CsvReader.py) in src/Input
2. In this file you need create a Class which extends InputAbstract Class
3. When extends InputAbstract class, you need implement the method read. This method receive filename and need return a dict
4. Create EXTENSIONS Constant with all file extensions will use the new input type. For this case is .csv. If you want implement yml, you can use .yml or .yaml
5. Use [JsonReader](src/Input/JsonReader.py) as example
6. In get_reader_class method from [Events Factory class](src/events/Factory.py), you need add the new input type. Don't forget import

```python
def get_reader_class(filename):
        _, file_extension = os.path.splitext(filename)
        if file_extension in JsonReader.JsonReader.EXTENSIONS:
            return JsonReader.JsonReader
        if file_extension in CsvReader.CsvReader.EXTENSIONS:
            return CsvReader.CsvReader
```

## Add new Output type

Like the input type process, in output type, the moving average app also uses Strategy Design Pattern.
If you want add new Output type like csv, yaml, xml, ... you need do the follow.
**Example**: Lets add xml input type

1. Create a file (XmlWriter.py) in src/Output
2. In this file you need create a Class which extends OutputAbstract Class
3. When extends InputAbstract class, you need implement the method write. This method receive Result Objects Array.
4. Create TYPES Constant with all ouput types which use the new ouput type. For this case is xml.
5. Use [JsonWriter](src/Output/JsonWriter.py) as example
6. In get_writer_class method from [Output Factory class](src/Output/Factory.py), you need add the new output type. Don't forget import

```python
def get_writer_class(output_type):
        if output_type in JsonWriter.JsonWriter.TYPES:
            return JsonWriter.JsonWriter
        if output_type in XmlWriter.XmlWriter.TYPES:
            return XmlWriter.XmlWriter
```