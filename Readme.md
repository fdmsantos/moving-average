# Description

Build a simple command line application that parses a stream of events and produces an aggregated output. 
In this case, we're interested in calculating, for every minute, a moving average of the translation delivery time for the last X minutes.

# Usage

```bash
./calculate_cli.py -h

./calculate_cli.py --input_file data/events.json --window_size 10 -o json
```

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

# CI/CD

Continuous integration / continuous delivery is implemented with circleCI

There are 3 Steps:

1. test -> Creates a docker container with python 3.6.7 image and run the tests
2. Build -> Creates a docker image based on Dockerfile
3. Publish -> Push the docker image to docker hub


# Log

Every time you run the app is run, is created a log file in data/log

# Extend Moving Average App

You are welcome to improve/add new features.
Please read this section before starts write new code

## Add new Input Type

The moving average app uses the Strategy Design Pattern to add new input type.
If you want add a new input type like csv, yaml, xml, ... you need to do the following.
**Example**: Let's add csv input type

1. Create a file (CsvReader.py) in src/Input
2. In this file, you need to create a Class which extends InputAbstract Class
3. When extends InputAbstract class, you need to implement the method read. This method receives filename and returns a dict
4. Create EXTENSIONS Constant with all file extensions will use the new input type. For this case is .csv. If you want to implement yml, you can use .yml or .yaml
5. Use [JsonReader](src/input/JsonReader.py) as example
6. In get_reader_class method from [Events Factory class](src/events/Factory.py), you need to add the new input type. Don't forget the import

```python
def get_reader_class(filename):
    _, file_extension = os.path.splitext(filename)
    if file_extension in JsonReader.JsonReader.EXTENSIONS:
        return JsonReader.JsonReader
    elif file_extension in CsvReader.CsvReader.EXTENSIONS:
        return CsvReader.CsvReader
    else:
        raise ...
```

## Add new Output type

Like the input type process, an output type, the moving average app also uses the Strategy Design Pattern.
If you want to add a new Output type like csv, yaml, xml, ... you need to do the following.
**Example**: Let's add xml input type

1. Create a file (XmlWriter.py) in src/Output
2. In this file, you need to create a Class which extends OutputAbstract Class
3. When extends InputAbstract class, you need to implement the method write. This method receives an Result Object Array.
4. Create TYPES Constant with all output types which use the new output type. For this case is xml.
5. Use [JsonWriter](src/output/JsonWriter.py) as example
6. In get_writer_class method from [Output Factory class](src/output/Factory.py), you need to add the new output type. Don't forget the import

```python
def get_writer_class(output_type):
    if output_type in JsonWriter.JsonWriter.TYPES:
        return JsonWriter.JsonWriter
    elif output_type in XmlWriter.XmlWriter.TYPES:
        return XmlWriter.XmlWriter
    else:
        raise ...

```


## Add new Validation to Event

The Event validation process uses the Chain of Responsibility Design Pattern.
**Example**: Let's add a validation to not permit the source_language and target_language are equals

1. Create a file (FieldsNotEquals.py) in src/events/validations/
2. In this file, you need to create a Class which extends RuleAbstract Class
3. When extends RuleAbstract class, you need to implement the method handle_request. This method returns false if the validation fails or run the next validation
4. Use [IsRequired](src/events/validations/IsRequired.py) as example

```python
def handle_request(self):
    if : # The condition to validation fail
        return False
    return self._successor.handle_request() if self._successor is not None else True
```

5. In get_validations method from [Events Factory class](src/events/Factory.py), you need add the new validation to the chain. Don't forget import and return the last validation

```python
rule11 = IsEquals(event, "event_name", rule10, "translation_delivered")
rule12 = IsDateTimeFormat(event, "timestamp", rule11, Event.TIMESTAMP_FORMAT)
newRule = FieldsNotEquals(event, "source_language|target_language", rule12)
return newRule
```


## Add new Aggregation Type

Is possible to add news aggregation types.
If you want to add new aggregation type like min, max, sum ... you need do the following.
**Example**: Let's add min aggregation type

1. Create a file (MovingMin.py) in src/aggregations
2. In this file, you need to create a Class which extends AggregationsAbstract Class
3. When extends AggregationsAbstract class, you need to implement the method calculate. This method receives the events and window size and returns the result
4. Create TYPE Constant with the type name. For this case is MIN.
5. Use [MovingAverage](src/aggregations/MovingAverage.py) as example
6. In calculate method from [Aggregations Factory class](src/aggregations/Factory.py), you need add the new aggregation type. Don't forget import

```python
def calculate(type, events, window_size):

    if type == MovingAverage.TYPE:
        aggregation = MovingAverage(
            events,
            window_size
        )
    elif type == MovingMin.TYPE:
             aggregation = MovingMin(
                 events,
                 window_size
             )
    else:
        raise AggregationNotSupportedException("Aggregation Type not supported")
    return aggregation.calculate()
```