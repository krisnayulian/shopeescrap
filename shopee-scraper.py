from datetime import date
import time
import requests

#print date to help users to track down when the file was generated.
data = date.today()
data.strftime("%d/%m/%Y")
data1 = date.today()

#asks for seller id.
seller_shopee_id = input('3939024838')

url_api_request = 'https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword=kremes%20ayam&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=e1aa84eb-1ab1-49c4-a2db-235a528d53c8' + seller_shopee_id
r = requests.get(url_api_request)

#define the number of ads published.
num_ads = (r.json()['data']['sections'][0]['data']['item'])
list_size = len(num_ads)

#creates a while statement using the number of ads created. Since the (index) json file stars with 0, the while statment starts with -1. 
creat_while = -1
while creat_while < list_size - 1:
    creat_while += 1
	
    #store the information displayed inside the json file. It's possible to extract even more data, you only need to add the exact json's children path you're interested in. The scrapper will sleep for 1 second and then get the next ad's information.
    ad_id = (r.json()['data']['sections'][0]['data']['item'][creat_while]['itemid'])
    title = (r.json()['data']['sections'][0]['data']['item'][creat_while]['name'])
    stock = (r.json()['data']['sections'][0]['data']['item'][creat_while]['stock'])
    sales = (r.json()['data']['sections'][0]['data']['item'][creat_while]['historical_sold'])
    likes = (r.json()['data']['sections'][0]['data']['item'][creat_while]['liked_count'])
    views = (r.json()['data']['sections'][0]['data']['item'][creat_while]['view_count'])
    price = (r.json()['data']['sections'][0]['data']['item'][creat_while]['price'])
    rating = (r.json()['data']['sections'][0]['data']['item'][creat_while]['item_rating']['rating_count'][0])
    time.sleep(1)

    #you've to set where you wanna save the csv file. If you run the code without changing the directory settings, you'll get no data.
    print(ad_id, '|', title, '|', stock, '|', price, '|', sales, '|', rating, '|', likes, '|', views, file=open("/your-directory/.csv" % data, "a"))

print('The scrapper is done. Your CSV file is ready!')
