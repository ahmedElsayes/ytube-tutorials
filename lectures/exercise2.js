/* 1- showing The event driven archticture in Node Js
2- Include an array to show how it work in JS
3- explain JSON (Parse / Strigify)
4- include work on File system from JS library
*/
console.log('Hello, we are arab programmers');
const events = require('events');
var eventemitter = new events.EventEmitter();
const fs = require('fs');

var record = [];

eventemitter.on('click',function(msg){
    // console.log(msg);
    record.push(msg);
    // console.log(record);
    var OB = JSON.parse(msg)
    // console.log(OB.city);
    console.log(OB);
    fs.appendFileSync('ASEEU.txt',record)
});

eventemitter.emit('click', '{ "name":"Ahmed", "age":30, "city":"cairo"}');
setTimeout(function(){
    eventemitter.emit('click', '{ "name":"Mohamed", "age":30, "city":"Alex"}'); 
},1000);
setTimeout(function () {
    eventemitter.emit('click', '{ "name":"Ali", "age":30, "city":"New York"}');
}, 3000);
setTimeout(function () {
    eventemitter.emit('click', '{ "name":"Hassan", "age":30, "city":"Alex"}');
}, 5000);
setTimeout(function () {
    console.log('code ended / Timeout')
}, 7000);