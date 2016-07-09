from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key="KD4iCiASW7FnTNzcatJN7Q",
    consumer_secret="vvHECsdN0Bvj9ShhxOa2KJWv_n0",
    token="-tnVOxd0VE8Wl7rOrTU12Fv1MEeCaU-",
    token_secret="jA8AwcCCVZz48oNycIjINAbUxRw"
)

client = Client(auth)
