// What is Recursion?


// {and what does: maxiumum call stack exceeded mean? what is the stack!?}


// ########## Looking at a function done two ways: with a loop, and with recursion ###########

//write a function which accepts a numberand returns the factorial of that number. a factorial is the
//product of an integer and all the integers below it. 
// factorial(1) // 1
// factorial(2) // 2
// factorial(4) // 24
// factorial(7) // 5040

// loop versions! loops loops loops loops loops loops loops loops loops loops loops loops loops 
function whileFactorial(num){
    var result = num;
    if (num === 0 || num === 1) return 1;
    while (num > 1) {
      num--;
      result *= num;
    }
    return result;
}
// console.log(whileFactorial(4))

function forFactorial(num) {
  if (num === 0 || num === 1) return 1;
  for (var i = num - 1; i >= 1; i--) {
    num *= i;
  }
  return num;
}
// console.log(forFactorial(4));


// recursive version!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
function factorial(num){
    if (num === 1){
        return 1
    }
    return num * factorial(num - 1);
}
// console.log(factorial(4))