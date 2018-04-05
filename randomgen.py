import requests
import json

def randomNumber():

    print("hi")
    
    url = "https://api.random.org/json-rpc/1/invoke"
    print("hi 2")

    data =    {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": "cbf83332-7d2a-4852-ba5b-dc6ec38e8328",
                "n": 6,
                "min": 1,
                "max": 6,
            },
        "id" : 6
        }

    json.dumps(data)
    print(json.dumps(data))
    
    print("hi 3")
    response = requests.post(url, data=json.dumps(data))
    print("hi 4")
    print(response)

    
    for i in response:
        print (i)
    
    
    return response

if __name__ == '__main__':
    randomNumber()