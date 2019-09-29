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

console.log(primeFromMN(10,49))



