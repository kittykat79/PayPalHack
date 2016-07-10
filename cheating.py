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
obj.actions()








	 