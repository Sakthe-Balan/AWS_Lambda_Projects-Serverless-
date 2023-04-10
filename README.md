# AWS_Lambda_Projects-Serverless-
1)Serverless Web Scraper using Lambda</br>(Code Present in the master branch)
built a web scraper using AWS Lambda. The scraper appears to scrape the course titles, URLs, and instructor names from the website of a university, and stores the data in an AWS DynamoDB table.</br>

The scraper is implemented using AWS Lambda, which is a serverless computing service that allows you to run code without having to manage servers. The code is triggered by an AWS CloudWatch Event on a scheduled basis, so that it runs at regular intervals to ensure that the data is up-to-date.</br>

The scraper uses the AWS SDK for Python (Boto3) to scrape the website and store the data in DynamoDB. Specifically, the scraper uses the requests library to make HTTP requests to the university's website, and the BeautifulSoup library to parse the HTML response and extract the course data. The data is then stored in a DynamoDB table using the put_item method from the boto3 DynamoDB client.</br>

Overall, the scraper has the following features:</br>

It uses AWS Lambda, which is a serverless computing service, to run the scraper code without having to manage servers.</br>
It uses AWS CloudWatch Events to trigger the scraper on a scheduled basis.</br>
It uses the requests library to make HTTP requests to the website being scraped.</br>
It uses the BeautifulSoup library to parse the HTML response and extract the course data.</br>
It uses AWS DynamoDB to store the scraped course data.</br>
It uses the boto3 DynamoDB client to interact with the DynamoDB table.</br>
It is written in Python, a widely-used programming language with a large number of libraries and frameworks available.</br>
