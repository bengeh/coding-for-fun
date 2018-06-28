package main

import (
    "fmt"
    "time"
    "math/rand"
)

type Message struct{
    Name string `json:"name"`
    Data interface{} `json:"data"`
}

type Client struct {
    send chan Message
}

func (client *Client) write(){
    for msg := range client.send{
        fmt.Printf("%#v\n", msg)
    }
}

func (client *Client) subscribeChannels(){
    for {
        time.Sleep(r())
        client.send <- Message{"channel add", ""}
    }
}

func (client *Client) subscribeMessages(){
    for {
        time.Sleep(r())
        client.send <- Message{"Message send", ""}
    }
}


func r() time.Duration{
    return time.Millisecond * time.Duration(rand.Intn(1000))
}

//go doesnt have constructors, create a function to set the data
func NewClient() *Client{
    return &Client{
        send: make(chan Message),
    }
}

//safely navigate through various go routine using channels
func main(){
    client := NewClient()
    go client.subscribeChannels() //first subroutine
    go client.subscribeMessages() //second subroutine
    client.write() //this is using the go routine when main is called
}