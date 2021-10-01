import json, requests ,random
url="http://localhost:8000/"
u3=requests.get(url+'addNew/'+str(random.randint(0,100)))
u3.text