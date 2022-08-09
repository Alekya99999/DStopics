from bs4 import BeautifulSoup
import requests
import lxml

import pandas as pd
import csv

soup = BeautifulSoup(requests.get("https://github.com/topics").text,'lxml')
#print(soup.prettify())

csv_file = open('topics.csv', 'w') 
writer = csv.writer(csv_file)
writer.writerow(['topicTitle','topicDescription','topicLink'])
csv_file.close()

topic_title_tags = soup.find_all('p', class_ = 'f3 lh-condensed mb-0 mt-1 Link--primary')
#print (topic_title_tags)

topic_Description_tags = soup.find_all('p', class_ = 'f5 color-fg-muted mb-0 mt-1')
#print (topic_Description_tags)        

topic_link_tags= soup.find_all('a', class_ = 'no-underline flex-grow-0')
#print(len(topic_link_tags))
#print("https://github.com" + topic_link_tags[0]['href'])


#print (topic_title_tags[0].text)

title_lists = []
for tags in topic_title_tags :
  title_lists.append(tags.text)


#print(title_lists)

description_lists = []
for tags in topic_Description_tags :
    description_lists.append(tags.text.strip())
    #print(description_lists)

link_lists = []
base_url = "https://github.com"
for tags in topic_link_tags :
    link_lists.append(base_url +tags['href'])
   # print(link_lists)


topic_Dictionaries = {

     'title' : topic_title_tags,
     'description' : topic_Description_tags,
     'links' : topic_link_tags
    }
    
    

topic_df = pd.DataFrame(topic_Dictionaries)
print(topic_df)





