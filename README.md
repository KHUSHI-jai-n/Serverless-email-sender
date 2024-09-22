# Serverless Email Sending application in AWS

## Table of Contents
1. [What the project is about](#what-the-project-is-about)
2. [Architecture](#architecture)
3. [How Lambda works](#how-lambda-works)
4. [Create a Lambda Role](#create-a-lambda-role)
5. [Send Email using SES and Lambda](#send-email-using-ses-and-lambda)
6. [Manage how to send using Step Functions](#manage-how-to-send-using-step-functions)
7. [Create the REST API Handler using Lambda](#create-the-rest-api-handler-using-lambda)
8. [Create and configure the API Gateway](#create-and-configure-the-api-gateway)
9. [Code a website and upload it to S3](#code-a-website-and-upload-it-to-s3)

## What the project is about
This project is a comprehensive AWS application that demonstrates the integration of various AWS services, including:
- S3
- API Gateway
- Lambda
- Step Functions
- SES
It provides a functional setup to send emails and manage requests via a REST API, all while remaining in the free tier.

## Architecture

## How Lambda works
AWS Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. You can execute code in response to events such as changes in data or system state, making it ideal for building scalable applications.

## Create a Lambda Role
To allow your Lambda function to access AWS services (like SES), you need to create a role with the necessary permissions. This role should have policies that grant access to SES ans Step Functions.

## Send Email using SES and Lambda
Amazon Simple Email Service (SES) is a cloud-based email sending service. In this project, we use SES to send emails triggered by AWS Lambda functions. The Lambda function contains the logic to format and send the email.

## Manage how to send using Step Functions
AWS Step Functions is a service that allows you to coordinate multiple AWS services into serverless workflows. In this project, Step Functions manage the execution flow, determining how emails are sent and handling errors gracefully.

## Create the REST API Handler using Lambda
A REST API Handler is a function that retrieves and processes data sent by a REST API. The objective is to create a Lambda function capable of receiving data sent by a REST API (body variable) and returning this data to the desired service (here Step Functions).

## Create and configure the API Gateway
The API Gateway acts as a front door for your application, allowing you to create, publish, and manage APIs at any scale. It integrates with your Lambda function to handle requests and route them accordingly.

## Code a website and upload it to S3
We developed a front-end website to interact with our backend services. This website is hosted on Amazon S3, allowing for easy access and deployment of static files.

## Conclusion
This project showcases how to utilize various AWS services to create a serverless application that can send emails. It serves as a practical example of cloud architecture and best practices.
