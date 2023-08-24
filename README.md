# Devops Technical Challenge

This repository contains an API that will add two numbers together via a GET request to the API endpoint. An [AWS SAM template](https://aws.amazon.com/serverless/sam/) is used to define the resources in IAC. The API was created in Python using the [FastAPI](https://fastapi.tiangolo.com/) framework.

**You can find the API hosted here:**

https://example.execute-api.us-east-1.amazonaws.com/sum/10/2

**Swagger Docs**

https://example.execute-api.us-east-1.amazonaws.com/docs

**Example Call**
```
curl https://example.execute-api.us-east-1.amazonaws.com/sum/10/2
```

## Project Requirements:
- [x] Initialized as a git repository
- [x] Using Infrastructure as code (SAM/CloudFormation)
- [x] Any language (Python)
- [x] Build and deploy an API endpoint
- [x] Accepts ```"GET /sum/{value1}/{value2}"```
- [x] Responds with the sum of two numbers in json ```"{ "sum": value_here }"```
- [x] Include a README.md file
    - **Stretch Goals:**
    - [x] Data input validation. The /sum endpoint accepts only "int" and "float" values.
    - [x] Code Tests. Includes tests via pytest to verify code functionality and input validation.
    - [x] Swagger documentation

## To build the SAM project you will need to install:
* [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Python 3.9

Start by cloning this repository to your local machine. Next, navigate to the directory where you cloned the files and run the command below.
```
sam build
```

### Deploy locally (using Docker) for development and testing
This requires Docker to be installed and running on your local machine.

Run this command from the root directory of the project.

```
sam local start-api
```

### Deploy the API to AWS
You will need to authenticate to your AWS account from the SAM CLI before deploying to AWS.

AWS uses an S3 bucket to store the Lambda deployment package. You can specify your own existing S3 bucket, or allow SAM CLI to create and manage one for you.
##### Deploy with managed default bucket
```
sam deploy --resolve-s3
```
##### Deploy with specified bucket
```
sam deploy --s3-bucket {S3BucketName}
```
