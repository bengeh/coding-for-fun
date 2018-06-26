package main
import (
    "fmt"
    "bufio"
    "os"
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


func main() {
    scanner := bufio.NewScanner(os.Stdin)
    fmt.Print("Enter your text: ")
    scanner.Scan()
    text := scanner.Text()
    word := LongestWord(text)
    fmt.Print(word)
    // for the factorial example 
    //fmt.Print("Enter your number: ")
    //scanner.Scan()
    //number := scanner.Text()
    //i, _ := strconv.Atoi(number)
    //Fact := FirstFactorial(i)
    //fmt.Print(Fact)
}
