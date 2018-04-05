import requests
import json
from PIL import Image
from pylab import imshow, show, get_cmap



def randomNumber():

    print("hi")
    
    url = "https://api.random.org/json-rpc/1/invoke"
    print("hi 2")

    data =    {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": "<insert-API-key here",
                "n": 50,
                "min": 0,
                "max": 100,
            },
        "id" : 6
        }

    json.dumps(data)
    print(json.dumps(data))
    
    print("hi 3")
    response = requests.post(url, data=json.dumps(data))
    print("hi 4")
    print(response)
    
    
    json_obj = response.json()
    print(json_obj['result']['random']['data'])
    
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