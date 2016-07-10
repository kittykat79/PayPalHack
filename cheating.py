from yelpauthdata import Yelp

class cheating(object):
	def __init__(self, action, target):
		self.action=action
		self.target=target

	def actions(self):
		if(self.action=="fix" and self.target=="doorknob"):
			yelp=Yelp()
			client=yelp.clientAuth()
			return client



obj = cheating("fix","doorknob")
client=obj.actions()

response = client.search('San Francisco')
print(response.businesses)
for i in range(3):
	print(response.businesses[i].name)








	 