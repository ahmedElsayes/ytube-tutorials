var http = require('http');
const request = require('request');
var express = require("express");
var bodyparser = require("body-parser");
var events = require('events');
var BitArray = require('node-bitarray');

var eventEmitter = new events.EventEmitter();
app = express();
app.use(bodyparser.json());

app.get('/', function (req,res){res.send("Hello world");});

app.post('/', function (req,res){
    res.send("Hello world");
    console.log(req.body);
    eventEmitter.emit('submit', req.body);
});

var options = {
    method: 'post',
    body: 	{"destUrl":"http://localhost:3000"}, // Javascript object payload
    json: true,
    url: "http://192.168.100.103/rest/services/startEvents"};
request(options, function (err, res, body) {
    if (err) {
        console.log('Error :', err);
        // return;
    }
});

eventEmitter.on('submit', function(msg){
    var ff = new Date();
    var sec = ff.getSeconds();
    // var binaries = sec.toString(2);
    var oo = BitArray.parse(sec);
    console.log(oo, sec);
    var invoke = {
        method: 'post',
        body: 	{"state0":Boolean(oo[0]),"state1":Boolean(oo[1]),"state2":Boolean(oo[3]),"state3":Boolean(oo[3]),"state4":Boolean(oo[4]),"state5":Boolean(oo[5]),"state6":false,"state7":false}, // Javascript object payload
        json: true,
        url: "http://192.168.100.103/rest/services/changeOutput"};

    // The following code to activate the outputs of the controller
    request(invoke, function (error, response, body) {
        if (error){console.log("Error: ", error);}
    });
});

app.listen(3000, function (){
    console.log("app running on port localhost:3000");});