import requests
from bs4 import BeautifulSoup
url_list_global=[]
url_list=[]
def resp(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_links = soup.find_all('div',class_='latest-prod-img')
    if all_links:
        for div_element in all_links:
            link_element=div_element.find('a')
            if link_element:
                url=link_element['href']
                url_list.append('mouthshut.com'+url)


url = 'http://www.mouthshut.com/category/Credit-Cards_reviews-925869.html'
resp(url)

for i in range(2,6):
    last_occurrence_index = url.rfind(".")
    resp(url[:last_occurrence_index] + '-page-'+str(i)+'.'+ url[last_occurrence_index+1:])
#     resp(url+'-page-'+str(i),url_list)

print(url_list)
print(len(url_list))

   
