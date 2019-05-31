// Algorithm Practice for Linear/Binear Search!

// Write a function that performs a linear search!
// Remember, if the value you're searching for is NOT found, return -1!
function linearSearch(arr, val) {
    // add whatever parameters you deem necessary - good luck!
}

// Write a function that performs a binary search!
// Remember, if the value you're searching for is NOT found, return -1!
function binarySearch(arr, val) {
    var start = 0;
    var end = arr.length - 1;
    var middle = Math.floor((start + end) / 2);
    // add whatever parameters you deem necessary - good luck!
}


// ########### NODE QUESTIONS! DO THESE FIRST! DISCUSS OUT LOUD!!!!!!! ############ //

    // •Differentiate between JavaScript and Node.js
    // •Differentiate between Node.js and Express
    // •What is npm ?
    // •What’s the difference between global and local installation of dependencies ?
    // •What is package.json ? What are some common attributes of package.json ?
    // •What is middleware ?
    // •Explain the purpose of module.exports
    // •Explain the MVC framework
    // •How can you avoid callback hell ?

// ############################################################################### //
// these are regular old algorithms for practice! not necessarily related to searching!

// #1 are there duplicates?
// write a function that accepts a variable number of arguments and checks whether there
// are any duplicates among the arguments passed in. 
// areThereDuplicates(1,2,3) // would return false
// areThereDuplicates(3,4,5,1,7,9,7) // would return true

function areThereDuplicates(){
    // Good luck!
}


// #2 max sub-array sum
// write a function that accepts an array of integers and a number. the function should
// find the maximum sum of a subarray with the length of the number passed in. Note that
// a subarray must consist of consecutive elements from the original array.
// maxSubArraySum([100,200,300,400], 2) // returns 700
// maxSubArraySum([-3,4,0,-2,6,-1], 2) // returns 5
// maxSubArraySum([1,4,2,10,23,3,1,0,20], 4) // returns 39

function subArraySum(){
    // Good luck!
}



// ############################ EXTRA CHALLENGING ################################# //
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the given number ?

function largestPrimeFactor(number) {
    // Good luck!
    return true;
}

largestPrimeFactor(13195);


// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two n - digit numbers.

function largestPalindromeProduct(n) {
    // Good luck!
    return true;
}

largestPalindromeProduct(3);

