import json, requests ,random
url="http://localhost:8000/"
u4=requests.get(url+'addNewError/'+str(random.randint(0,100)))
u4.text