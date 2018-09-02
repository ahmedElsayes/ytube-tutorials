// simple logical operations with if condition
var x = 6;
var y = 8;
var z = 7;
if (x > z && y > z){
console.log("the result is true");
}
else{console.log("false")}

if (x > z || y < z){
console.log("the result is true");
}
else{console.log("false");}
// find the maximum among group of numbers
// (2 5 48 6 9 15 3 8)
function findmax(){
var max = 0;
var i;
for(i = 0; i < arguments.length; i++){
if(arguments[i] > max){
	max = arguments[i];
}
}
return max
}

// find the minimum among group of numbers
function findmin(){
var min = 1000000000;
var j;
for(j = 0; j < arguments.length; j++){
if(arguments[j] < min){
	min = arguments[j];
}
}
return min
}
var R = findmax(45,5,48,6,9,99,3,8);
var T = findmin(45,5,48,6,9,99,3,8);
console.log("maximum = ",R,"  minimum = ",T);

// class building
function person(first, second, age, hight, eye){
	this.firstname = first;
	this.secondname = second;
	this.age = age;
	this.hight = hight;
	this.eyecolor = eye;
}

// we want to build subclasses
var friend1 = new person("Ahmed","Mohamed",25,180,"brown")
var friend2 = new person("hazem","Mohamed",29,182,"black")
var friend3 = new person("mahmoud","Mohamed",27,176,"brown")

// building method
friend1.fulldescription = function(){
	return this.firstname + " " + this.secondname + ", his age is" + this.age; 
}
console.log("the full description of the first friend",friend1.fulldescription(),"the name of second friend is",friend2.firstname + " " + friend2.secondname);

// implement inside Html file



