let students = ["Liz", "Brodie", "Reagan", "Tom", "Jack F", "Ben", "Jack M", "Evan",
    "Thomas", "Igor", "RJ", "Pierson", "JC", "Angel", "Austin", "Danny", "Eli"]

function getRandom(arr){
    return Math.floor(Math.random() * arr.length)
}

function shuffle(arr){
    let shuffledStudents = []
    while(arr.length !== 0){
        let random = getRandom(arr)
        let thisStudent = arr.splice(random, 1)
        shuffledStudents.push(thisStudent[0])
    }
    return shuffledStudents
}

console.log(shuffle(students))

