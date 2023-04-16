# AWS_Lambda_Projects-Serverless-

## Serverless Web Scraper using Lambda(Code Present in the master branch)
</br>
built a web scraper using AWS Lambda. The scraper appears to scrape the course titles, URLs, and instructor names from the website of a university, and stores the data in an AWS DynamoDB table.</br>

The scraper is implemented using AWS Lambda, which is a serverless computing service that allows you to run code without having to manage servers. The code is triggered by an AWS CloudWatch Event on a scheduled basis, so that it runs at regular intervals to ensure that the data is up-to-date.</br>

The scraper uses the AWS SDK for Python (Boto3) to scrape the website and store the data in DynamoDB. Specifically, the scraper uses the requests library to make HTTP requests to the university's website, and the BeautifulSoup library to parse the HTML response and extract the course data. The data is then stored in a DynamoDB table using the put_item method from the boto3 DynamoDB client.</br>

Overall, the scraper has the following features:</br>

It uses AWS Lambda, which is a serverless computing service, to run the scraper code without having to manage servers.</br>
It uses AWS CloudWatch Events to trigger the scraper on a scheduled basis.</br>
It uses the requests library to make HTTP requests to the website being scraped.</br>
It uses the BeautifulSoup library to parse the HTML response and extract the course data.</br>
It uses AWS DynamoDB to store the scraped course data.</br>
It uses the boto3 DynamoDB client to interact with the DynamoDB table.</br
It is written in Python, a widely-used programming language with a large number of libraries and frameworks available.</br></br>

## EC2 Instance Start-Stop Lambda Function

This Lambda function starts and stops an EC2 instance based on a CloudWatch event rule. The function is triggered by a CloudWatch event at a specified time, and uses the AWS SDK for Python (boto3) to start or stop an EC2 instance based on the event.

## Setup

1. Create an IAM role for the Lambda function with permissions to interact with EC2 instances and CloudWatch events. Attach the `AmazonEC2FullAccess` and `CloudWatchEventsFullAccess` policies to the role.

2. Create a new Lambda function in the AWS Management Console or using the AWS CLI. Use the provided code as a starting point.

3. Set up a CloudWatch event rule to trigger the Lambda function at the desired time. The rule should be based on a cron expression that specifies the time and frequency of the event.

4. Update the function code with the correct EC2 instance ID and region.

5. Test the function by manually triggering it using the Lambda console or the AWS CLI.

## Usage

The function is triggered automatically by the CloudWatch event rule. When triggered, the function checks the current state of the specified EC2 instance, and either starts or stops the instance based on the state.

## License

This code is released under the MIT License. See LICENSE.md for more information.

