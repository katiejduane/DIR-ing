//write a function which accepts a numberand returns the factorial of that number. a factorial is the
//product of an integer and all the integers below it.
// factorial(1) // 1
// factorial(2) // 2
// factorial(4) // 24
// factorial(7) // 5040

function factorial(num) {
  
}


// write a function called power which accepts a base and an exponent,the function should return
// the power of the base to the exponent
// 2 to the power of 4 = 2*2*2*2

function power(base, exponent) {
  
}


//write a function called productOfArray that takes in array of nums and returns the product of them all!
// productOfArray([1,2,3]) // 6
// productOfArray([1,2,3,10]) // 60

function productOfArray(arr) {
  
}


//write a function called recursive range which accepts a number and adds up all the numbers from 0
//to the number passed to the function.
// recursiveRange(6) // 21
// recursiveRange(10) // 55

function recursiveRange(num) {
  if (num === 0) return num;
  return num + recursiveRange(num - 1);
}
// console.log(recursiveRange(4))

//write a function called fib which accepts a number and returns the nth number in the fibonacci
//sequence. 1,1,2,3,5,8,13,21,34,55
// fib(4) // 3
// fib(10) // 55
// fib(28) // 317811
// fib(35) // 9227465

function fib(n) {
  
}


//write a function that reverses a string recursively
// reverse(cloud) // duolc

function reverse(str) {
  
}


// write a function that uses recursion to take an array of arrays and returns a new
// array with all the values flattened
// flatten([1, 2, 3, [4, 5] ]) // [1, 2, 3, 4, 5]
// flatten([1, [2, [3, 4], [[5]]]]) // [1, 2, 3, 4, 5]
// flatten([[1],[2],[3]]) // [1,2,3]
// flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) // [1,2,3]

function flatten(arr){

}


// write a recursive function that returns the sum of all even numbers in an object which
// may contain nested objects
function nestedEvenSum() {
  // add whatever parameters you deem necessary
}

// EXAMPLES OF THIS ONE --------------->

// var obj1 = {
//   outer: 2,
//   obj: {
//     inner: 2,
//     otherObj: {
//       superInner: 2,
//       notANumber: true,
//       alsoNotANumber: "yup"
//     }
//   }
// }

// var obj2 = {
//   a: 2,
//   b: {b: 2, bb: {b: 3, bb: {b: 2}}},
//   c: {c: {c: 2}, cc: 'ball', ccc: 5},
//   d: 1,
//   e: {e: {e: 2}, ee: 'car'}
// };

// nestedEvenSum(obj1); // 6
// nestedEvenSum(obj2); // 10














// ===================================== SOLUTIONS ===================================== //

function factorial(num) {
  if (num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
// console.log(factorial(4))


function power(base, exponent) {
  if (exponent === 0) return 1;
  return base * power(base, exponent - 1);
}
// console.log(power(2,6))


function productOfArray(arr) {
  if (arr.length === 0) {
    return 1;
  }
  return arr[0] * productOfArray(arr.slice(1));
}
// console.log(productOfArray([1,2,3,4,5]))


function recursiveRange(num) {
  if (num === 0) return num;
  return num + recursiveRange(num - 1);
}
// console.log(recursiveRange(4))


function fib(n) {
  if (n <= 2) return 1;
  console.log(n-1, n-2)
  return fib(n - 1) + fib(n - 2);
}
console.log(fib(8));


let stringToRev = "cloud";
function reverse(str) {
  if (str.length <= 1) {
    return str;
  }
  return reverse(str.substr(1)) + str[0];
}
// console.log(reverse(stringToRev));


function flatten(oldArr) {
  var newArr = [];
  for (var i = 0; i < oldArr.length; i++) {
    if (Array.isArray(oldArr[i])) {
      newArr = newArr.concat(flatten(oldArr[i]));
    } else {
      newArr.push(oldArr[i]);
    }
  }
  return newArr;
}


function nestedEvenSum(obj, sum = 0) {
  for (var key in obj) {
    if (typeof obj[key] === "object") {
      sum += nestedEvenSum(obj[key]);
    } else if (typeof obj[key] === "number" && obj[key] % 2 === 0) {
      sum += obj[key];
    }
  }
  return sum;
}