// function showInfo(fname, lname, eyes, hair){
//     return fname + lname + eyes + hair
// }

var mom = {
    firstName: 'Alice',
    lastName: 'Wong',
    eyeColor: 'brown',
    hairColor: 'black',

    showInfo: function(){
        return `${this.firstName} ${this.lastName} Hair color: ${this.hairColor} Eye Color: ${this.eyeColor}`
    }
};

var daughter = {
    __proto__: mom,
    firstName: 'Ilene',
    hairColor: 'brown'
};

console.log(mom.showInfo())
console.log(daughter.showInfo())