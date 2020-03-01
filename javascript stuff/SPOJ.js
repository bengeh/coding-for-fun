/*
TABLE OF CONTENT
1. afterFortyTwo
2. primeFromMN
3. primeFromMN
4. isSubStr
5. nextPalindrome
6. gotFixedPoint
7. commonElements
8. canPartition
9. findPosElement
10. printCountOfLetter
11. firstNonRepeatingElement
12. minimumAbsoluteDiff
13. formBiggestNumber
14. 
*/
/*
Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. 
More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. 
All numbers at input are integers of one or two digits.
*/
var afterFortyTwo = function(n){
	for(var i = 0; i < n.length; i++){
		if(n[i] == 42){
			break
		}
		console.log(n[i])
	}
}

//afterFortyTwo([1,88,2,3,42,5,6])
//afterFortyTwo([42,1,88,2,3,42,5,6])


/*Prime number generator: print every prime number between m and n*/
//using segmented sieve
var simpleSeive = function(limit, prime){
	var arr = new Array(limit + 1).fill(false)
	for(var i = 2; i <= limit; i++){
		if(arr[i] == false){
			prime.push(i)
			for(var j = i; j <= limit; j+= i){
				arr[j] = true
			}
		}
	}
	
}

var primeFromMN = function(m, n){
	var limit = Math.floor(Math.sqrt(n)) + 1
	var prime = []
	simpleSeive(limit, prime)
	var res = []
	var range = n - m + 1
	var mark = new Array(range + 1).fill(false)
	
	
	for(var i = 0; i < prime.length; i++){
		var lowLim = Math.floor(m / prime[i]) * prime[i]
		if(lowLim < m || lowLim == prime[i]){
			lowLim += prime[i]
		}
		for(var j = lowLim; j <= n; j+=prime[i]){
			mark[j - m] = true
		}
	}
	for(var i = m; i <= n; i++){
		if(!mark[i-m]){
			res.push(i)
		}
	}
	return res
}

//console.log(primeFromMN(10,49))




/*
Check if pattern is substring of text
Solution: Using KMP algorithm
*/
var computeTempKMPArr = function(pattern){
	var arr = new Array(pattern.length)
	var index = 0
	var i = 1
	while(i < pattern.length){
		if(pattern[i] == pattern[index]){
			arr[i] = index + 1
			index++
			i++
		}else{
			if(index != 0){
				index = arr[index-1]
			}else{
				arr[i] = 0
				i ++
			}
		}
	}
	return arr
}

var isSubStr = function(mainText, comparePattern){
	var comArr = computeTempKMPArr(comparePattern)
	var i = 0 
	var j = 0
	while(i < mainText.length && j < comparePattern.length){
		if(mainText[i] == comparePattern[j]){
			i++
			j++
		}else{
			if(j != 0){
				j = comArr[j-1]
			}else{
				i++
			}
		}
	}
	if(j == comparePattern.length){
		return true
	}
	return false
}

//console.log(isSubStr('abcdefasds', 'gfe'))

/*

Given a number, find the next smallest palindrome larger than this number. For example, if the input number is “2 3 5 4 5”, the output should be “2 3 6 3 2”.
 And if the input number is “9 9 9”, the output should be “1 0 0 1”.
The input is assumed to be an array. Every entry in array represents a digit in input number. Let the array be ‘num[]’ and size of array be ‘n’
*/

var nextPalindrome = function(num){
	num = Array.from(String(num), Number)
	
	var size = num.length
	var mid = Math.floor(size/2)
	var left = mid - 1
	var right = (size % 2 == 0) ? mid : mid + 1
	var leftSmaller = false
	
	while(left >= 0 && num[left] == num[right]){
		left--
		right++
	}
	
	if(left < 0 || num[left] < num[right]){
		leftSmaller = true
	}
	while(left >= 0){
		num[right++] = num[left--]
	}
	
	if(leftSmaller){
		var carry = 1
		
		if(size % 2 == 1){
			num[mid] += 1
			carry = num[mid]/10
			num[mid] %= 10
		}
		left = mid - 1
		right = (size%2==0) ? mid : mid + 1
		while(left >= 0){
			num[left] = num[left] + carry
			carry = num[left]/10
			num[left] %= 10
			num[right] = num[left]
			left--
			right++
		}
	}
	return num

}

// console.log(nextPalindrome(783322))

/*
Find a Fixed Point (Value equal to index) in a given array
Given an array of n distinct integers sorted in ascending order, write a function that returns a Fixed Point in the array, if there is any Fixed Point present in array, else returns -1. 
Fixed Point in an array is an index i such that arr[i] is equal to i. 
Note that integers in array can be negative.

Input: arr = [-10, -5, 0, 3, 7]
Output: 3 arr[3] == 3

*/
var gotFixedPoint = function(arr){
	var front = 0
	var end = arr.length 

	while(front <= end){
		var mid = Math.floor((front+end) / 2)
		if(arr[mid] == mid){
			return mid
		}
		if(arr[mid] < mid){
			front = mid + 1
		}else{
			end = mid - 1
		}
	}
	return -1
}

// console.log(gotFixedPoint([0, 2, 5, 8, 17]))

/*
Find common elements in three sorted array
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output = 20, 80
*/
var commonElements = function(arr1, arr2, arr3){
	var i = 0
	var j = 0
	var k = 0
	var res  = []
	while(i < arr1.length && j < arr2.length && k < arr3.length){
		if(arr1[i] == arr2[j] && arr1[i] == arr3[k]){
			res.push(arr1[i])
			i++
			j++
			k++
		}
		else if(arr1[i] < arr2[j]){
			i++
		}
		else if(arr2[j] < arr3[k]){
			j++
		}
		else{
			k++
		}
	}
	return res
}
// console.log(commonElements([1,5,10,20,40,80], [6,7,20,80,100], [3,4,15,20,30,70,80,120]))
// console.log(commonElements([1, 5, 5], [3, 4, 5, 5, 10], [5, 5, 10, 20]))

/*
Partition problem is to determine whether a given set can be 
partitioned into two subsets of equal sum

arr = [1, 5, 11, 5]
output: true (partitioned into [1,5,5] and [11])

soln: 
1. Find total of array, if odd, return false as there wouldnt be able
to have 2 subsets with equal sum
2. Find sum / 2. 
3. Find a subset of array where sumOfSubSet == sum/2
*/
var canPartition = function(arr){
	var total = 0
	for(var i = 0; i < arr.length; i++){
		total += arr[i]
	}
	if(total % 2 != 0){
		return false
	}

	return helper(arr, 0, 0, total)
}

var helper = function(arr, idx, sum, total){
	if(sum * 2 == total){
		return true
	}
	if(sum * 2 > total || idx > arr.length){
		return false
	}
	return helper(arr, idx + 1, sum, total) || helper(arr, idx + 1, sum + arr[idx], total)	

}

// console.log(canPartition([1,5,5,11]))

/*
Find number of positional elements
Given a matrix of integers, task is to find out number of positional elements. 
A positional element is one which is either minimum or maximum in a row or in a column.

1 3 4
5 2 9
8 7 6

min: 1,2,6,4
max: 8,7,9

*/

var findPosElement = function(matrix){
	var row = matrix.length
	var col = matrix[0].length
	var rowMaxNo = new Array(row)
	var rowMinNo = new Array(row)
	var colMaxNo = new Array(col)
	var colMinNo = new Array(col)


	for(var i = 0; i < row; i++){
		var rowMin = Number.MAX_SAFE_INTEGER
		var rowMax = Number.MIN_SAFE_INTEGER
		for(var j = 0; j < col; j++){
			if(matrix[i][j] < rowMin){
				rowMin = matrix[i][j]
			}
			if(matrix[i][j] > rowMax){
				rowMax = matrix[i][j]
			}
		}
		rowMaxNo[i] = rowMax
		rowMinNo[i] = rowMin
	}
	console.log(rowMaxNo)
	console.log(rowMinNo)

	for(var i = 0; i < col; i++){
		var colMin = Number.MAX_SAFE_INTEGER
		var colMax = Number.MIN_SAFE_INTEGER
		for(var j = 0; j < row; j++){
			if(matrix[j][i] < colMin){
				colMin = matrix[j][i]
			}
			if(matrix[j][i] > colMax){
				colMax = matrix[j][i]
			}
		}
		colMaxNo[i] = colMax
		colMinNo[i] = colMin
	}
	console.log(colMaxNo)
	console.log(colMinNo)

}
// findPosElement([[1,3,4], [5,2,9], [8,7,6]])

/*
Given a string "aaabbbcccdaa" return a3b3c3d1a2
*/

var printCountOfLetter = function(str){
	var curChar = str[0]
	var curCount = 1
	var res = ''
	var i = 1
	while(i <= str.length){
		if(str[i] == curChar){
			curChar = str[i]
			curCount++
		}
		else if(str[i] != curChar){
			res = res + curChar + curCount
			curChar = str[i]
			curCount = 1
		}
		i++
	}
	return res
}
// console.log(printCountOfLetter("aaabbbcccda"))

/*
First non-repeating element in an array
[-1, 2, -1, 3, 2] output: 3

[-1 2]
solonum 2
*/

var firstNonRepeatingElement = function(arr){
	var hashSet = new Map()
	for(var i = 0; i < arr.length; i++){
		if(!hashSet.has(arr[i])){
			hashSet.set(arr[i], 1)
		}else{
			hashSet.set(arr[i], hashSet.get(arr[i]) + 1)
		}
	}
	for([k,v] of hashSet){
		if(v == 1){
			return k
		}
	}
	return -1
}
// console.log(firstNonRepeatingElement([-1, 2, -1, 3, 2]))

/*
Given an array, find the minimum absolute difference of the array
1 -3 71 68 17
output: 3 (71-68)
*/
var minimumAbsoluteDiff = function(arr){
	res = new Array(arr.length).fill(Number.MAX_SAFE_INTEGER)
	for(var i = 1; i < arr.length; i++){
		var j = 0
		while(j < i){
			res[i] = Math.min(res[i], Math.abs(arr[j] - arr[i]))
			j++
		}
	}
	var minVal = Number.MAX_SAFE_INTEGER
	for(var i = 0; i < res.length; i ++){
		if(res[i] < minVal){
			minVal = res[i]
		}
	}
	return minVal
}
// console.log(minimumAbsoluteDiff([-59,-36,-13,1,-53,-92,-2,-96,-54,75]))

/*
Given an array of numbers, arrange them in a way that yields the largest value. 
For example, if the given numbers are {54, 546, 548, 60}, 
the arrangement 6054854654 gives the largest value. 

1. the trick here is to extend the given number to the longest number length + 1
for this case: 5454, 5465, 5485, 6060
2. sort it in desc order
3. then print out the original int

*/
var formBiggestNumber = function(arr){
	var l = Math.max(...arr).toString().length + 1
	var temp = ''
	var extVal = []
	var extMap = new Map()
	for(var i = 0; i < arr.length; i++){
		temp = arr[i].toString().repeat(l)
		extVal.push(temp.substr(0, l))
		extMap.set(temp.substr(0, l), arr[i])
	}
	extVal.sort((a,b) => (b-a))
	var res = ''
	for(var i = 0; i < extVal.length; i++){
		console.log(extMap.get(extVal[i]))
		res = res + extMap.get(extVal[i]).toString()
	}
	return res
}
// console.log(formBiggestNumber([54, 546, 548,60]))

var printShape = function(n){
	for(var i = n/2; i > 0; i--){
		for(var j = 0; j < i * 2; j++){
			if(i % 2 == 0){
				console.log("o")
			}else{
				console.log("x")
			}
		}
		console.log("\n")
	}
	var k = (2*n) - 2
	for(var i = 0; i < n/2; i++){
		for(var j = 0; j < k; j++){
			k = k - 2
		}
		for(var j = 0; j < (i + 1) * 2; j++){
			if(i % 2 ==0){
				console.log("x")
			}else{
				console.log("o")
			}
		}
		console.log("\n")
	}
}

printShape(10)









