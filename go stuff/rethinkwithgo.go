package main

import(
    "fmt"
    r "github.com/dancannon/gorethink"
)

type User struct {
    Id string `gorethink:"id,omitempty"`
    Name string `gorethink:"name"`
}

func main(){
    session, err := r.Connect(r.ConnectOpts{
        Address: "localhost:28015",
        Database: "randomDataBase",
    })
    
    if err != nil {
        fmt.Println(err)
        return
    }
    
    //To insert user into table user
    /*
    user := User{
        Name: "meh",
    }
    response, err := r.Table("user").Insert(user).RunWrite(session) //RunWrite will return a response unlike .Exec()
    
    if err != nil {
        fmt.Println(err)
        return
    }
    */
    
    /*
    //To update table
    user := User {
        Name: "NewName",
    }
    response, _ := r.Table("user").Get("425244ef-54dd-4a9b-a84c-87bb9ddb45e3").Update(user).RunWrite(session)
    */
    /*
    //To delete an item
    response, _ := r.Table("user").Get("425244ef-54dd-4a9b-a84c-87bb9ddb45e3").Delete().RunWrite(session)
    
    fmt.Printf("%#v\n" , response)
    
    */
    
    //showing real time updates
    /*
    cursor, _ := r.Table("user").Changes(r.ChangesOpts{IncludeInitial: true}).Run(session)
    
    var changeResponse r.ChangeResponse
    for cursor.Next(&changeResponse){
        fmt.Printf("%#v\n", changeResponse)
    }
    */
    

    
    
    
    
    
    
    
}