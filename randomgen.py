import requests
import json
from PIL import Image
from numpy import random

def randomNumber():

    print("hi")
    
    url = "https://api.random.org/json-rpc/1/invoke"
    print("hi 2")

    data =    {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": "cbf83332-7d2a-4852-ba5b-dc6ec38e8328",
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
    print("inside rgb")
    print(random.random((50,50)))
    img = Image.new( 'RGB', (255,255), "black") # create a new black image
    pixels = img.load() # create the pixel map
    no = randomNumber()
    no1 = randomNumber()
    for i in no:    # for every pixel:
        for j in no1:
            pixels[i,j] = (i, j, 100) # set the colour accordingly

    img.show()
    


    
    
    
    
if __name__ == '__main__':
    #randomNumber()
    rgbpicture()