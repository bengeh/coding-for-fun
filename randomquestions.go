package main
import (
    "fmt"
    "bufio"
    "os"
    "strconv"
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

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    fmt.Print("Enter your number: ")
    scanner.Scan()
    number := scanner.Text()
    i, _ := strconv.Atoi(number)
    Fact := FirstFactorial(i)
    fmt.Print(Fact)
}
