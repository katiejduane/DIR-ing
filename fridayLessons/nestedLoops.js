
// for(let i = 0; i < 5; i++){
//     let row = "";
//     for(let j = 0; j < 5; j++){
//         row = row + "X"
//     }
//     console.log(row);
// }

function printBox(width, height) {
  let row = "";
  for (let i = 0; i < height; i++) {
    row = "";
    // silly hack to make the dev tools show the whole square
    // row = row + i;
    for (let j = 0; j < width; j++) {
      if (i === 0 || i === height - 1) {
        row = row + "X";
      } else if (j === 0 || j === width - 1) {
        row = row + "*";
      } else {
        row = row + " ";
      }
    }
    console.log(row);
  }
}

printBox(6, 4)

