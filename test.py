from selenium import webdriver
from bs4 import BeautifulSoup
from get_urls import url_list
import pandas as pd
column_name = ["Reviews","Bank"]

final=[]
list_df=[]
bank=[]

def extract_review(url):

    driver = webdriver.Chrome()
    driver.get(f"https://www.{url}")
  
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    review_divs = soup.find_all("div", class_="more reviewdata")
    for review_div in review_divs:
        p_tags = review_div.find_all("p")
        for p_tag in p_tags:
            last_slash_index = url.rfind('/') 
            bank_index = url.rfind('reviews')     
            if last_slash_index != -1 and bank_index != -1:
                result = url[last_slash_index + 1:bank_index]
                bank.append(result[:-1])
            review_text = p_tag.get_text().strip() 
            final.append(review_text)
    driver.quit()


for i in url_list:
    extract_review(i)
    

print(final)
print(len(final))
print(len(bank))



data = {'Reviews': final, 'Bank': bank}
df = pd.DataFrame(data)
df.to_csv("scraper_part/review_final.csv")