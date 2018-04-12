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
                "apiKey": "cbf83332-7d2a-4852-ba5b-dc6ec38e8328",
                "n": 128,
                "min": 0,
                "max": 500,
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
    Z = [randomNumber()] * 128   # Test data
    imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
    show()
    
    
if __name__ == '__main__':
    #randomNumber()
    rgbpicture()