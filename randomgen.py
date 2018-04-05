import requests
import json
from PIL import Image
from pylab import imshow, show, get_cmap

def randomNumber():
    url = "https://api.random.org/json-rpc/1/invoke"
    data =    {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": "<insert-API-key here>",
                "n": 50,
                "min": 0,
                "max": 100,
            },
        "id" : 6
        }
    json.dumps(data)
    response = requests.post(url, data=json.dumps(data))
    json_obj = response.json()
    
    return json_obj['result']['random']['data']


def rgbpicture():

    img = Image.new( 'RGB', (255,255), "black") # create a new black image
    pixels = img.load() # create the pixel map
    Z = [randomNumber(), randomNumber()]   # Test data
    imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
    show()
    
    
if __name__ == '__main__':
    #randomNumber()
    rgbpicture()