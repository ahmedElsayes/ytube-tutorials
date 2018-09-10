console.log('starting notes.js');

// process   &  moduls
// console.log(module);

exports.math = function(a,b){
console.log('mathematical operations on a&b','add', a+b,'multibly', a*b,'divid', a/b);
return a+b;
};

exports.recentyear = 2018;

// class building
function person(first, second, age, hight, eye) {
    this.firstname = first;
    this.secondname = second;
    this.age = age;
    this.hight = hight;
    this.eyecolor = eye;
}

// we want to build subclasses
var friend1 = new person("Ahmed", "Mohamed", 25, 180, "brown")
var friend2 = new person("hazem", "Mohamed", 29, 182, "black")
var friend3 = new person("mahmoud", "Mohamed", 27, 176, "brown")

// building method
friend1.fulldescription = function () {
    return this.firstname + " " + this.secondname + ", his age is" + this.age;
}

exports.friend1 = friend1.fulldescription();