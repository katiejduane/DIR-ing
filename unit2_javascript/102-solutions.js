// function printNumbers(start, end) {
//   for (let i = start; i <= end; i++) {
//     console.log(i);
//   }
// }

function printSquare(size) {
  let row = '';
  for (let i = 0; i < size; i++) {
    row = '';
    for (let j = 0; j < size; j++) {
      row = row + '*';
    }
    console.log(row);
  }
}

printSquare(5)


function printBox(width, height) {
  let row = '';
  for (let i = 0; i < height; i++) {
    row = '';
    // silly hack to make the dev tools show the whole square
    // row = row + i;
    for (let j = 0; j < width; j++) {
      if (i === 0 || i === (height - 1)) {
        row = row + '*';
      } else if (j === 0 || j === (width - 1)){
        row = row + '*';
      } else {
        row = row + ' ';
      }
    }
    console.log(row);
  }
}

// function makeRow(length, char) {
//   let row = '';
//   for (let i = 0; i < length; i++) {
//     row = row + char;
//   }
//   return row;
// }

// function printBanner(message) {
//   console.log(makeRow(message.length + 4, '*'));
//   console.log('* ' + message + ' *');
//   console.log(makeRow(message.length + 4, '*'));
// }


// function _rotate(array, original, amount) {
//   var rotatedValue = original;

//   var index = array.indexOf(original);

//   // Don't rotate by multiples of the length of the array.
//   amount = amount % array.length;

//   if (index !== -1) {
//     index = index + amount;

//     if (index >= array.length) {
//       index = index - array.length;
//     }

//     rotatedValue = array[index];
//   }
//   return rotatedValue;
// }

// function caesar(message, amount) {
//   const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
//   if (!amount) {
//     amount = 13;
//   }

//   let newMessage = '';
//   for (let i=0; i < message.length; i++) {
//     newMessage = newMessage + _rotate(alphabet, message[i], amount);
//   }

//   return newMessage;
// }

// function _leetLookup(char) {
//   let val = char;
//   const dictionary = {
//     A: 4,
//     E: 3,
//     G: 6,
//     I: 1,
//     O: 0,
//     S: 5,
//     T: 7
//   }
//   if (dictionary[char] !== undefined) {
//     val = dictionary[char];
//   }
//   return val;
// }

// function leetspeak(message) {
//   let newMessage = '';
//   message = message.toUpperCase();
//   for (let i = 0; i < message.length; i++) {
//     newMessage = newMessage + _leetLookupArrayy(message[i])
//   }
//   return newMessage;
// }

// function _leetLookupArray(char) {
//   let letters = 'aegiost'.toUpperCase().split('');
//   let numbers = '4361057'.toUpperCase().split('');
//   let val = char;

//   if (char in letters) {
//     val = numbers[letters.indexOf(char)];
//   }

//   return val;
// }

// function longLongVowels(message) {
//   let newMessage = '';
//   let alphabet = 'aeiou'.split('');
//   for (let i=0; i < message.length; i++) {
//     if (alphabet.indexOf(message[i]) !== -1) {
//       // console.log('found ' + message[i]);
//       if (i !== message.length - 1) {
//         if (message[i] === message[i + 1]) {
//           // console.log('before ' + newMessage);
//           newMessage = newMessage + message[i] + message[i] + message[i];
//           // console.log('after ' + newMessage);
//         } else {
//           newMessage = newMessage + message[i];
//         }
//       }
//       // console.log('after2 ' + newMessage);
//     } else {
//       newMessage = newMessage + message[i];
//       // console.log('after3 ' + newMessage);
//     }
//   }

//   return newMessage;
// }

// function sumNumbers(arr) {
//   let result = 0;
//   for (let i=0; i < arr.length; i++) {
//     result = result + arr[i];
//   }
//   return result;
// }

// function positiveNumbers(arr) {
//   let result = [];
//   for (let i=0; i < arr.length; i++) {
//     if (arr[i] >= 0) {
//       result.push(arr[i]);
//     }
//   }
//   return result;
// }

// function matrixAdd(m1, m2) {
//   // This might be easier if they were in a single array.
//   var all = [m1, m2];
//   var result = [];

//   // Create an array of arrays (with zeros).
//   result = m1.map(function (row) {
//     return row.map(function () {
//       return 0;
//     });
//   });

//   // Go through each matrix, adding its elements to
//   // the final tally.
//   result = all.reduce(function (tally, matrix) {
//     matrix.forEach(function (row, i) {
//       row.forEach(function (cell, j) {
//         result[i][j] = result[i][j] + cell;
//       });
//     });
//     return result;
//   }, result);

//   return result;
// }
// // console.log(matrixAdd([[1, 3], [2, 4]], [[5, 2], [1, 0]]));

// // Using student-contributed solution :)
// function matrixMultiply(matrix1, matrix2) {
//     let row = 0;
//     let col = 0;
//     let row2 = 0;
//     let result = [[0, 0], [0, 0]];
// //GOES THROUGH ROWS OF THE FIRST MATRIX
//     while(row < 2){
//         // result[row] = [];
// // GOES THROUGH COLUMNS OF THE SECOND MATRIX
//         while(col < 2){
// // GOES THROUGH ROWS OF THE SECOND MATRIX
//             while(row2 < 2){
//                 result[row][col] += matrix1[row][row2] * matrix2[row2][col];
//                 row2++;
//             }
//             row2 = 0;
//             col++;
//         }
//         col = 0;
//         row++;
//     }

//     return result;
// }


// function rockPaperScissors(move1, move2) {
//   if (move1 === move2) {
//       // same move
//       return 'draw';
//   } else if (move1 === 'rock') {
//       if (move2 === 'paper') {
//           // paper wraps rock
//           return 'player 2';
//       } else {
//           // rock smashes scissors
//           return 'player 1';
//       }
//   } else if (move1 === 'paper') {
//       if (move2 === 'rock') {
//           // paper wraps rock
//           return 'player 1';
//       } else {
//           // scissors cut paper
//           return 'player 2';
//       }
//   } else if (move1 === 'scissors') {
//       if (move2 === 'rock') {
//           // rock smashes scissors
//           return 'player 2';
//       } else {
//           // scissors cut paper
//           return 'player 1';
//       }
//   }
// }

// function rowIsAllSame(row) {
//     return (row[0] === row[1]) && (row[0] === row[2]);
// }

// function flipRowsAndColumns(gameBoard) {
//     let newBoard = [
//                     [null, null, null],
//                     [null, null, null],
//                     [null, null, null],
//                     ];
//     for (let y=0; y<gameBoard.length; y++) {
//         let row = gameBoard[y];
//         for (let x=0; x<row.length; x++) {
//             // Flip our coordinates from y,x to x,y
//             newBoard[x][y] = row[x];
//         }
//     }
//     return newBoard;
// }

// function diagonalIsSame(gameBoard) {
//     return (
//         gameBoard[0][0] === gameBoard[1][1] &&
//         gameBoard[0][0] === gameBoard[2][2]
//     ) || (
//         gameBoard[0][2] === gameBoard[1][1] &&
//         gameBoard[0][2] === gameBoard[2][0]
//     );
// }

// function ticTacToe(gameBoard) {
//     // Did someone win a row?
//     const rowWinner = gameBoard.filter(function (row) {
//         return rowIsAllSame(row);
//     });

//     // If we have any rows, that row contains the winning player.    
//     if (rowWinner.length > 0) {
//         return rowWinner[0][0];

//     // Did someone win a diagonal?
//     } else if (diagonalIsSame(gameBoard)) {
//         return gameBoard[1][1];

//     } else {
//         // Did someone win a column?

//         // "Rotate" the board so that columns are now rows.
//         const flippedBoard = flipRowsAndColumns(gameBoard);

//         // Filter out any "row" that doesn't have all the same player.
//         const columnWinner = flippedBoard.filter(function (row) {
//             return rowIsAllSame(row);
//         });
//         // If we have any rows, that row contains the winning player.
//         if (columnWinner.length > 0) {
//             return columnWinner[0][0];
//         }
//     }
// }