
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import os
print(os.getcwd())

fi=open(os.getcwd()+'/'+'config_secret.json','r') 
creds = json.load(fi)
auth = Oauth1Authenticator(**creds)
client = Client(auth)
response = client.search('San Francisco')
print(response.businesses)
for i in range(3):
	print(response.businesses[i].name)
	