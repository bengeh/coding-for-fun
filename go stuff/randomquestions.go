package main
import (
    "fmt"
    //"bufio"
    //"os"
   // "strconv"
   "regexp"
   "log"
   "strings"
)

//Factorial example for Golang
func FirstFactorial(num int) int { 

  // code goes here   
  // Note: feel free to modify the return type of this function 
  if num == 0{
    return 1
}
    return num * FirstFactorial(num-1)
            
}

//Longest word challenge
func LongestWord(text string) string{
    
    reg, err := regexp.Compile("[^a-zA-Z]+")
    
    if err != nil{
        log.Fatal(err)
    }
    
    processedString := reg.ReplaceAllString(text, " ")
    
    words := strings.Fields(processedString)
    
    longestword := 0
    answer := ""
    
    for _, element := range words{
        if len(element) > longestword{
            longestword = len(element)
            answer = element
        }
    }
    fmt.Print(longestword)
    fmt.Print(answer)
    
    return answer
}

//reverse word challenge
func ReverseWord(text string) string{
    
    runes := []rune(text)
    for i,j := 0, len(runes) - 1; i<j;i, j = i + 1, j - 1{
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)

}


func main() {

    //for the reverse challenge
    /*
    scanner := bufio.NewScanner(os.Stdin)
    fmt.Print("Enter your text: ")
    scanner.Scan()
    text := scanner.Text()
    word := ReverseWord(text)
    fmt.Print(word)
    */
    
    //understanding maps in Golang
    //create a map for fun
    var m = make(map[string]int)
    m["route"] = 66
    fmt.Print(m)
    
    //check if there's a key called 'route' then print it's value
    a, ok := m["route"]
    if ok{
        fmt.Print(a)
    }
    
    //printing out the map
    for key, value := range m{
        fmt.Print("key: ", key, "Value: ", value)
    }

    //for the longest word challenge
    /*scanner := bufio.NewScanner(os.Stdin)
    fmt.Print("Enter your text: ")
    scanner.Scan()
    text := scanner.Text()
    word := LongestWord(text)
    fmt.Print(word)
    */
    
    /*
    // for the factorial example 
    fmt.Print("Enter your number: ")
    scanner.Scan()
    number := scanner.Text()
    i, _ := strconv.Atoi(number)
    Fact := FirstFactorial(i)
    fmt.Print(Fact)
    */
}
