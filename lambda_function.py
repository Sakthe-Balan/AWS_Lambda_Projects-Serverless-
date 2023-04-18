import json
import requests
from bs4 import BeautifulSoup
import csv
import time
from requests.exceptions import RequestException
from urllib3.exceptions import ProtocolError
import boto3


def lambda_handler(event, context):

   
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('courses')
    headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "DNT": "1", "Connection": "close",
                    "Upgrade-Insecure-Requests": "1"}
    for i in range(1,661):
                k=3
                # Define the URL of the webpage containing the links to be scraped
                url = 'https://www.classcentral.com/provider/udemy?page=' + str(i)
            
                # Define the headers to be used for making requests to the website
              
            
                # Send a GET request to the website and parse the HTML content using BeautifulSoup
                while True:
                    try:
                        page = requests.get(url, headers=headers)
                        break
                    except (RequestException, ProtocolError) as e:
                        print(f"Error: {e}")
                        time.sleep(5) # wait for 5 seconds before retrying
                        continue
                    
                    except AttributeError:
                        print("Error: 'NoneType' object has no attribute 'content'")
                        time.sleep(2) # wait for 2 seconds before retrying
                        continue
                    
                    except requests.exceptions.ChunkedEncodingError:
                        print("Error: 'ChunkedEncodingError' occurred while decoding response content")
                        time.sleep(2) # wait for 2 seconds before retrying
                        continue
                
            
                soup1 = BeautifulSoup(page.content, 'html.parser')
                soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
            
                # Define the CSV file and attributes
                
            
                # Loop through all the links in the webpage and scrape the data inside each of them
                for link in soup2.find_all('a', attrs={'class': 'color-charcoal course-name'}):
                    link_url = link['href']
                    link_url = 'https://www.classcentral.com' + link_url
                    print(link_url,i)
                    if(link_url=='https://www.classcentral.com/course/udemy-copywriter-32281 121'):
                        continue
            
                    # Send a GET request to the link and parse the HTML content using BeautifulSoup
                    while (k):
                        try:
                            link_page = requests.get(link_url, headers=headers)
                            link_soup1 = BeautifulSoup(link_page.content, 'html.parser')
                            link_soup2 = BeautifulSoup(link_soup1.prettify(), 'html.parser')
                            time.sleep(3)
                            
                        
            
                            # Scrape the data inside the link using BeautifulSoup
                            try:
                                Image = link_soup2.find('img', attrs={'class': 'absolute'}).get('src').strip()
                            except AttributeError:
                                print("Image not available. Retrying in 3 seconds...")
                                time.sleep(3)
                                k-=1
                                continue
                                
                            try:
                                title = link_soup2.find('h1', attrs={'class': 'head-2'}).get_text().strip()
                            except AttributeError:
                                print("Title not available. Retrying in 3 seconds...")
                                time.sleep(3)
                                k-=1
                                continue
                                
                            try:
                                Overview = link_soup2.find('div', attrs={'class': 'wysiwyg'}).get_text().strip()
                            except AttributeError:
                                print("Overview not available. Retrying in 3 seconds...")
                                time.sleep(3)
                                k-=1
                                continue
                                
                            try:
                                div = link_soup2.find('div', attrs={'class': 'course-noncollapsable-section'})
                                p = div.find('p', attrs={'class': 'text-1'})
                                taught_by = p.get_text().strip()
                                Link = link_soup2.find('a', attrs={'class': 'btn-blue btn-medium width-100 padding-horz-xlarge'}).get(
                                    'href').strip()
                                Link = 'https://www.classcentral.com' + str(Link)
                            except AttributeError:
                                print("Link not available. Retrying in 3 seconds...")
                                time.sleep(3)
                                k-=1
                                continue
                                
                            try:  
                                rating = link_soup2.find('span', attrs={'class': 'color-gray margin-top-xxsmall'}).get_text().strip()
                            except AttributeError:
                                print("rating not available. Retrying in 3 seconds...")
                                time.sleep(3)
                                k-=1
                                continue
                                
                                
            
                            # Write the data to the CSV file
                            data = {
                                            'title': str(title),
                                            'Image':str( Image),
                                            'overview': str(Overview),
                                            'taught_by':str(taught_by),
                                            'link': str(link),
                                            'rating': str(rating)
                                        }
                            table.put_item(Item=data)

                            break
                        except AttributeError:
                                print("Data not available. Retrying in 5 seconds...")
                                time.sleep(2)
   
   
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }