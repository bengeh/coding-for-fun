package main
import (
    "fmt"
    "bufio"
    "os"
   "strconv"
   "regexp"
   "log"
   "strings"
   "unicode"
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


//creating a random map
func MapCreation() {
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
}

//Letters substituition
func swapText(str string) string{
  // code goes here   
  // Note: feel free to modify the return type of this function 
  out := []rune(str)
  for i:=0; i<len(out); i++{
      if unicode.IsLetter(out[i]){
          if out[i] == 122{
              out[i] = 97
          }else if out[i] == 32{
              out[i] = 32
          }else{
              out[i] += 1
          }
            switch out[i]{
                  case 97:
                    out[i] = 65
                    case 101:
                    out[i] = 69
                    case 105:
                    out[i] = 73
                    case 111:
                    out[i] = 79
                    case 117:
                    out[i] = 85
              }
      }
  }
  return string(out)
            
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    fmt.Print(`
    1. Reverse Challenge
    2. Longest Word Challenge
    3. Factorial Challenge
    4. Map Example
    5. Letters substituition
    Please choose a number: `)
    scanner.Scan()
    switch text := scanner.Text(); text{
        case "1":
            fmt.Println("This is the reverse challenge")
            fmt.Print("Enter your text here: ")
            scanner.Scan()
            reverseText := scanner.Text()
            word := ReverseWord(reverseText)
            fmt.Print(word)
        case "2":
            fmt.Println("This is for the longest word challenge")
            fmt.Print("Enter your text here: ")
            scanner.Scan()
            longText := scanner.Text()
            word := LongestWord(longText)
            fmt.Print(word)
        case "3":
            fmt.Println("This is the factorial example")
            fmt.Print("Enter your number: ")
            scanner.Scan()
            number := scanner.Text()
            i, _ := strconv.Atoi(number)
            Fact := FirstFactorial(i)
            fmt.Print(Fact)
        case "4":
            fmt.Println("This is how a map looks like in Go")
            MapCreation()
        case "5":
            fmt.Println("This is how you substitute letters to the next (A->B, Z->A, a->b, z->a, vowels are caps, and all non-letters remain as they are")
            fmt.Println("Enter your letter: ")
            scanner.Scan()
            letter := scanner.Text()
            Swapped := swapText(letter)
            fmt.Print(Swapped)
        default:
            fmt.Println("Default")
    }
}
