import json
from ebaysdk.finding import Connection as Finding

keywords = ['Car']
postalCode = ['95101']
api = Finding(domain='svcs.sandbox.ebay.com', appid="Shashwat-spendsma-SBX-e99eeec0d-a6b019b8", config_file=None)
response = api.execute('findItemsAdvanced', {'keywords': 'Car', 'sortOrder': 'PricePlusShippingLowest', 'buyerPostalCode': postalCode})

print(json.dumps(response.dict(),indent=4))
