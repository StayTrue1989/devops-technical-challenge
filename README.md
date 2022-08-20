# Devops Technical Challenge

This repository contains an API that will add two numbers together via a GET request to the API endpoint. An [AWS SAM template](https://aws.amazon.com/serverless/sam/) is used to define the resources in IAC. The API was created in Python using the [FastAPI](https://fastapi.tiangolo.com/) framework.

## Requirements:
- [x] Using Infrastructure as code (SAM/CloudFormation)
- [x] Any language (Python)
- [x] Build and deploy an API endpoint
- [x] Accepts ```"GET /sum/{value1}/{value2}"```
- [x] Responds with the sum of two numbers in json ```"{ "sum": value_here }"```


## Stretch Goals:
- [x] Data input validation. The /sum endpoint accepts only "int" and "float" input values.
- [x] Python code tests using pytest. Includes tests to verify input validation only accepts int and float values.
- [x] Swagger documentation for the API



## To deploy the API to AWS
Start by cloning this repository to your local machine. Next, navigate to the directory where you cloned the files and run the commands below.

##### 1. Build step
```
sam build
```
##### 2. Deploy step
AWS Cloudformation uses an S3 bucket to store the Lambda deployment package. You can specify your own existing S3 bucket, or allow SAM CLI to create and manage one for you.
##### Deploy with managed default bucket
```
sam deploy --resolve-s3
```
##### Deploy with specified bucket
```
sam deploy --s3-bucket {S3BucketName}
```

## To deploy locally (using Docker) for development and testing
This requires Docker to be installed and running on your local machine.  Run the command from the directory containing the AWS SAM template. This creates a local HTTP server in a docker container.
```
sam local start-api
```
