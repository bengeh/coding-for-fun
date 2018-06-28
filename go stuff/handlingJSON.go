package main

import(
    "encoding/json"
    "fmt"
    "github.com/mitchellh/mapstructure"
)

type Message struct {
    Name string `json:"name"`
    Data interface{} `json:"data"`
}

type Channel struct {
    Id string `json:"id"`
    Name string `json:"name"`
}

func main() {
    recRawMsg := []byte(`{"name":"channel add",` + `"data":{"name":"Hardware Support"}}`)
    var recMessage Message
    err := json.Unmarshal(recRawMsg, &recMessage)
    if err != nil {
        fmt.Println(err)
        return
    }
     fmt.Printf("%#v\n", recMessage)
     
     if recMessage.Name == "channel add"{
        channel, err := addChannel(recMessage.Data)
        var sendMessage Message
        sendMessage.Name = "channel add"
        sendMessage.Data = channel
        sendRawMsg, err := json.Marshal(sendMessage)
        if err != nil{
            fmt.Println(err)
            return
        }
        fmt.Printf(string(sendRawMsg))
    }

}
//takes in a data parameter and returns Channel and error
func addChannel(data interface{}) (Channel, error){
    var channel Channel
    //channelMap := data.(map[string]interface{}) //the '.' here to indicate a type assertion, that data is a map of string with values of empty interface
    //channel.Name = channelMap["name"].(string) //type assertion again, saying that the value of channelMap["name"] is a string
    
    //or can use third party library (mapstructure by mitchellh)
    err := mapstructure.Decode(data, &channel)
    if err != nil{
        return channel, err //can only return nil for pointer types
    }
    
    channel.Id = "1"
    fmt.Printf("%#v\n", channel)
    return channel, nil
}