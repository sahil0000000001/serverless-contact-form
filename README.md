# Serverless Contact Form (AWS)

## Project Overview
This project implements a serverless backend to store website contact form submissions using AWS services.

## Architecture
Frontend (HTML + JS)
→ API Gateway (HTTP API)
→ AWS Lambda (Python)
→ DynamoDB

## AWS Services Used
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

## How It Works
1. User submits contact form from website
2. Frontend sends POST request to API Gateway
3. API Gateway triggers Lambda function
4. Lambda stores data in DynamoDB
5. Data can be viewed in DynamoDB console

## Screenshots
Screenshots are available in the `screenshots/` folder:
- API Gateway Invoke URL
- API Routes
- DynamoDB stored items
- Lambda execution logs

## Skills Demonstrated
- Serverless architecture
- REST API integration
- AWS Lambda (Python)
- DynamoDB NoSQL database
- Cloud monitoring with CloudWatch

