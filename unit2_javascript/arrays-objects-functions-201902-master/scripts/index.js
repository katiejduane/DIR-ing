// Positive Numbers
// Write a function which takes an array of numbers as input and returns a new array containing only the positive numbers in the given array.
// arr = [-5, 4, -3, 2, -1, 0, 45, 8282, -3939]
function positiveNumbers(arr) {
  let positiveArr = [];
  for (i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      positiveArr.push(arr[i]);
    }
  }
  return positiveArr;
}

function filterEvenNumbers(arr) {
  let newArr = arr.filter(one => one % 2 === 0);
  return newArr;
}

//3 times
//Given this function:
//Use the call3Times function to print "Hello, world!" 3 times.
function speak() {
  console.log("Hello, world!");
}

function call3Times(fun) {
  fun();
  fun();
  fun();
}

function callNTimes(times, fun) {
  for (let i = 0; i < times; i++) {
    fun();
  }
}

// Write a strMultiply function which takes two arguments:

// str - the string to multiply
// times - number of times to multiply
// Example:

// > strMultiply('abc', 5)
// 'abcabcabcabcabc'
// You may not use the native repeat method that strings provide.But you can use the range function defined below.

// You may use the following range function as is:

function strMultiply(str, times) {
  const arr = [];
  function range(min, max) {
    for (var i = min; i < max; i++) {
      // arr.push(i);
      arr.push(str);
    }
    return arr;
  }
  range(0, times);
  // let newArray = arr.map(item => item = str);
  let newString = arr.join("");
  return newString;
}

//Cities 1
//Write a function which takes an array of city objects like such:
//as input and returns a new array containing the cities whose temperature is cooler than 70 degrees.

const cities = [
  { name: "Los Angeles", temperature: 60.0 },
  { name: "Atlanta", temperature: 52.0 },
  { name: "Detroit", temperature: 48.0 },
  { name: "New York", temperature: 80.0 }
];

//Cities 2
//Write a function which takes an array of city objects like the above problem as input and returns an array of the cities names.

function names(cities) {
  let cityNames = [];
  cities.forEach(function(city) {
    cityNames.push(city.name);
  });
  console.log(cityNames);
}

//Good Job!
//Given an array of people's names:
//Print out 'Good Job, {{name}}!' for each person's name, one on a line.

const people = [
  "Dom",
  "Lyn",
  "Kirk",
  "Autumn",
  "Trista",
  "Jesslyn",
  "Kevin",
  "John",
  "Eli",
  "Juan",
  "Robert",
  "Keyur",
  "Jason",
  "Che",
  "Ben"
];

function goodJob(peeps) {
  peeps.forEach(function(onePeep) {
    console.log(`${onePeep}, treat yo'self!`);
  });
}

//Sort an array
//Given an array of strings such as the array of names given in one of the "Good Job" problem, sort them by alphabetically order.
function sortAlpha(peeps) {
  peeps.sort();
  return peeps;
}

//Sort an array, 2
//Sort the same array, but not by alphabetically order, but by how long each name is, shortest name first.
function sortLongyMcLongName(peeps) {
  function compare(a, b) {
    return a.length - b.length;
  }
  peeps.sort(compare);
  return peeps;
}

// Sort an array, 3
//Given an array of array of products:
//Sort the array by price.
const products = [
  { name: "Basketball", price: 12.0 },
  { name: "Tennis Racquet", price: 66.0 },
  { name: "Tennis Balls", price: 9.0 },
  { name: "Tennis Balls", price: 9.0 }
];
function sortPrices(products) {
  function compare(a, b) {
    return a.price - b.price;
  }
  products.sort(compare);
  return products;
}

//GoT
console.log(`There are ${characters.length} characters in the array.`);

// How many characters names start with "A"?
function charA(characters) {
  let arrA = characters.filter(one => one.name[0] === "A");
  console.log(arrA.length);
}
// How many characters names start with "Z"?
// How many characters are dead?
function deaded(characters) {
  let deadChars = characters.filter(one => one.died != "");
  console.log(deadChars.length);
}
// Who has the most titles?
function titles(characters) {
  let rackinEmUp = characters.filter(one => one.titles.length);
}
// How many are Valyrian?
// What actor plays "Hot Pie" (and don't use IMDB)?
// How many characters are *not* in the tv show?
// Produce a list characters with the last name "Targaryen"
// Create a histogram of the houses (it's the "allegiances" key)
function houseOgram(characters) {
  let houses = characters.filter(one => one.allegiances != "");
  let numHouses = {};
  houses.forEach(function(house) {
    if (house != numHouses) {
    }
  });
}

//Student's; I refactored
function mostTitle(characters) {
  let count = 0;

  characters.forEach(function(array) {
    if (array.titles.length > count) {
      count = array.titles.length;
      name = array.name;
    }
  });
  console.log(
    `Who has the most titles?: ${name} \n Number of titles: ${count}`
  );
}

//Student's
function targaryen(characters) {
  let name = [];
  let list = [];
  characters.forEach(function(array) {
    name = array.name.split(" ");
    if (name[name.length - 1] == "Targaryen") {
      list.push(array.name);
    }
  });
  console.log(list);
}
