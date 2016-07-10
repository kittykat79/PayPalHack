from yelpauthdata import Yelp

class cheating(object):
	def __init__(self, target):
		self.target=target

	def targets(self):
		yelp=Yelp()
		client=yelp.clientAuth()
		params = {'term': self.target, 'lang': 'en','deals_filter':'true'}
		response=client.search('San Jose', **params)
		print(response.businesses)
		for i in range(3):
			print(response.businesses[i].name)
		return client
	




obj = cheating("doorknob")
client=obj.targets()



#response = client.search('San Francisco')









	 