import requests
import smtplib
import googlemaps
import pandas

api_key = "AIzaSyBYNzJbVl-fwx-YmjcKgsE1tBpz3Ziwyn4"
map_client = googlemaps.Client(api_key)

type = ['store', 'shop', 'destination', 'local']
places_result = map_client.places_nearby(location = '39.76762532574416, -86.15918731673908', radius = 100000, open_now = False, type = type)

mydf = pd.DataFrame()
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
count =0
for place in places_result['results']:
    my_place_id = place['place_id']
    my_fields = ['name','vicinity','type', 'website', 'rating', 'price_level']
    place_details = map_client.place(place_id = my_place_id, fields = my_fields)
    
    if 'vicinity' in place_details['result'] and 'website' in place_details['result'] and 'rating' in place_details['result'] and 'price_level' in place_details['result']:
        if place_details['result']['types'][0] != 'liquor_store': 
            l1.append(place_details['result']['name'])
            l2.append(place_details['result']['types'][0])
            l3.append(place_details['result']['rating'])   
            l4.append(place_details['result']['website'])
            l5.append(place_details['result']['vicinity'])
            l6.append(place_details['result']['price_level'])
    
mydf['name'] = l1
mydf['type'] = l2
mydf['rating'] = l3
mydf['address'] = l5
mydf['website'] = l4
mydf['price'] = l6
mydf
mydf.to_csv('data.csv', index=False)

newdf = pd.DataFrame()

time = 0
while time < 8:
    count=0
    max=0
    row=-1
    temp=0
    for i in mydf['rating']:
        temp = i
        if(temp > max):
            max = temp
            row = count
        count+=1
    
    time += 1
        
    newdf = newdf.append(mydf.iloc[row])
    mydf = mydf.drop(mydf.index[row])
    
    
time = 9
start_time = []
end_time = []
ttime = []
x = 0
for i in newdf['price']:
    if time > 12:
        time-=12
        x = 1
    if x == 0 and time != 12:
        start_time.append(str(time) + " AM")
    else:
        start_time.append(str(time) + " PM")
    
    ttime.append(str(i) + " hours")
    
    time += (i)
    if (x==1) and (time > 9):
        del ttime[-1]
        ttime.append(str(9 - (time-i)) + ' hours')
        time = 9
        
        
    if time > 12:
        time-=12
        x = 1
    if x == 0 and time != 12:
        end_time.append(str(time) + " AM")
    else:
        end_time.append(str(time) + " PM")
        

newdf['start_time'] = start_time
newdf['end_time'] = end_time
newdf['time'] = ttime
del newdf['rating']
del newdf['price']
newdf = newdf.reset_index()

count = 0
x = 0
for i in newdf['end_time']:
    #print(i)
    #print(i == '9 PM')
    #print()
    if x == 0 and i == '9 PM':
        x = 1
    if x == 1 and i == '9 PM':
        break
    count+=1

newdf = newdf.head(count+1)
newdf.to_csv('plan.csv', index=False)
