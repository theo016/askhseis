import urllib.request
import json
import datetime, time


day = datetime.datetime.today().strftime ('%d')
month = datetime.datetime.today().strftime ('%m')
year = datetime.datetime.today().strftime ('%Y')


if ((datetime.datetime.now().strftime("%H:%M:%S")) < str("08:00:00")): #Το κινο έχει αλλάξει την ώρα της πρώτης κλήρωσης σε 8:00 απο 9:00 , 
                                                                       #για τους προηγούμενους μήνες το σωστό είναι να ελέγχει εάν η ώρα είναι πριν τις 9:00
    days = int(day)-1
else:
    days = int(day)
    
def get_stats(stats):
    url = f"https://api.opap.gr/draws/v3.0/1100/{li1[0]}"
    r = urllib.request.urlopen(url)
    html= r.read()
    html = html.decode()
    li2 = json.loads(html)
    return li2[stats]["list"]

all = [0]*(days*20)
eachday =[0]*20

for c in range (1, days+1):
    date = f'{year}-{month}-{c:02d}'
    url1 = f"https://api.opap.gr/draws/v3.0/1100/draw-date/{date}/{date}/draw-id"
    r1= urllib.request.urlopen(url1)
    html1 = r1.read()
    html1 = html1.decode()
    li1 = json.loads(html1)
    
    for results in range (0, 20):
        eachday[results] = (get_stats("winningNumbers")[results])
       
    all.extend(eachday)
  

for n in range (1, 81):
    if all.count(n)!=0:
        print ("Το", n, "κληρώθηκε", all.count(n), "φορές")
    
        
    else:
        print ("Το", n, "δεν κληρώθηκε")



