function flatten(arr) {

  var temp = [];

  function recursiveFlatten(arr) { 
    for(var i = 0; i < arr.length; i++) {
      if(Array.isArray(arr[i])) {
        recursiveFlatten(arr[i]);
      } else {
        temp.push(arr[i]);
      }
    }
  }
  recursiveFlatten(arr);
  console.log(temp)
  return temp;
}


// flatten([1,2,3,4,[5,4,[4]]])


//permutation
var permutate = function(nums){
    var used =[], res =[]
    helper(nums, [], res, used)
    console.log(res)
    return res
}

var helper = function(nums, tmpArr, res, used){
    if(tmpArr.length == nums.length){
        res.push(tmpArr.slice(0))
        return
    }

    for(var i = 0; i < nums.length; i++){
        if(!used[i]){
            used[i] = true
            tmpArr.push(nums[i])
            helper(nums,tmpArr, res, used)
            used[i] = false
            tmpArr.pop()
        }
    }

}

// permutate([1,2,3])


//permutate string
var permutateStr = function(str){
    var res = []
    helper('', str, res)
    console.log(res)
    return res
}

var helper = function(prefix, suffix, result){
    if(suffix.length == 0){
        result.push(prefix)
        return
    }
    for(var i = 0; i < suffix.length; i++){
        helper(prefix + suffix.charAt(i), suffix.substr(0, i) + suffix.substr(i + 1, suffix.length), result)
    }
}

// permutateStr("abc")



/*
Write a function solution that, given two integers A and B, returns a string
containing exactly A letters 'a' and B letters 'b' with no 3 consecutive
letters being the same (no 'aaa' or 'bbb' may occur)
*/
function solution(A,B){
  var result ='', len = A+B, lenA=0,lenB=0
  for(var i = 0; i < len; i++){
    if((A>B && lenA < 2) || (B > A && lenB >= 2) || (A==B && result[i-1] =='b')){
      result += 'a'
      lenA++
      lenB=0
      A--
    }else if((B>A && lenB<2) || (A > B && lenA >=2) || (A==B)){
      result+='b'
      lenB++
      lenA=0
      B--
    }
  }
  return result
}

/*
Write a function that given an array A of N integers represting the time of
execution of consecutive tasks, return true if it is posisble for
the load balancer to choose two requests that will determine an
even distribution of requests among three workers, or false otherwise


Given A =[1,3,4,2,2,2,1,1,2], function should return true, as choosing
index 2 (value is 4) and index 5 (value is 2) results in a distribution giving 4 seconds of handling time to each
work

resulting array would be [1,3,2,2,1,1,2]
can be split equally among 3 workers with max value of 4
*/ 


/*

change string from abbccc to ab2c3
if string only have 1 character just print it, if have more, print 
the counter next to it

*/
function compressedString(message){
  var count = 1
  var res = ''
  var idx = 0

  while(idx < message.length){
    var currLetter = message[idx]
    var counter = 1
    idx++
    while(message[idx] == currLetter){
      counter++
      idx++
    }
    if(counter == 1){
      res = res + currLetter
    }
    else if(counter != 1){
      res = res + currLetter + counter
    }
  }
  return res
}

/*
  Robot wants to pick strawberries from a bush.
  Given an integer array arr of length n and an integer num
  as input where num is the number of strawberries a robot will
  pick as maximum. Each array element in arr represents the number of
  strawberries present in each bush and n is the number of bushes.
  A robot cannot pick from two consecutive bushes and it has to
  pick the strawberries in such a way that it may not exceed the
  limit proposed, num. Find the maximum number of strawberries
  a robot can pick.

  Example:
  100
  5
  50 10 20 30 40
  output:
  90


*/

function maxStrawberries(numArr, max){
  var res = 0
  if(numArr == null || numArr.length == 0){
    return 0
  }
  var helper = function(nums, cur, tmp, m){
    if(tmp > m){
      return
    }
    res = Math.max(tmp, res)
    for(var i = 2; i < nums.length; i++){
      for(var j = cur; j+i < nums.length; j++){
        helper(nums, i+j, tmp + nums[i + j], m)
      }
    }
  }
  for(var i = 0; i < numArr.length; i++){
    helper(numArr, i, numArr[i], max)
  }

  return res
}

console.log(maxStrawberries([10,50,10], 100))