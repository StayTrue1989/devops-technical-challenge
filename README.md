# devops-technical-challenge

This repository contains an AWS SAM template that can be used to deploy the "Sum" API to AWS.

# Requirements:
- [x] Using Infrastructure as code (SAM/CloudFormation)
- [x] Any language (Python)
- [x] Build and deploy an API endpoint
- [x] Accepts ```"GET /sum/{value1}/{value2}"```
- [x] Responds with the sum of two numbers in json ```"{ "sum": value_here }"```


# Stretch Goals:
- [x] Data input validation. The /sum endpoint accepts only "int" and "float" input values.
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
