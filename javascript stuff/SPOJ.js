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

console.log(isSubStr('abcdefasds', 'gfe'))


















