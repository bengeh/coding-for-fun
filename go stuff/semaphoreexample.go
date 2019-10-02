package main

import (
	"sync"
	"fmt"
)

/*  
	- Using semaphores in channels for concurrent programs
    - Channels arent resources like files or sockets, you dont need to close
    them to free them
    - Release locks and semaphores in the reverse order you acquired them
    - Goroutine is easy and light to implement, however the goroutine using resources such
    as files, sockets, bandwidth could be a lot, hence can use semaphores to help
    - Acquire semaphores when you're ready to use them
	- Before you start a goroutine, always know when and how it will exit
	- Avoid mixing anonymous functions and goroutines
*/

func printNum() int{
	fmt.Println("inside find error")
	nums := []int{1,2,3,4,5}
	intChan := make(chan int, len(nums)) //Cater to all nums job error channel
	sem := make(chan int, 4) // 4 jobs running at once

	var wg sync.WaitGroup
	wg.Add(5)
	for i := range nums{
		go worker(i, sem, &wg, intChan)
	}

	wg.Wait()
	close(intChan)

	return <- intChan
}

func worker(num int, sem chan int, wg *sync.WaitGroup, intChan chan int){
	defer wg.Done()
	sem <- 1
	fmt.Println(num)
	<- sem
}


func main(){
	printNum()
}