// code designed by Ahmed Elsayes    student No. 272537      "ahmed.elsayes@student.tut.fi"
var ws = require("./WS");

var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);
// const http = require('http');
const request = require('request');

app.use(express.static(__dirname + '/public'));
//redirect / to our index.html file
app.get('/invoker', function(req, res,next) {
    res.sendFile(__dirname + '/public/index.html');
});

// const hostname = '127.0.0.1';
// const port = 3000;
// events to subscribe to it
//http://localhost:3000/RTU/SimROB7/services/LoadPallet
//http://localhost:3000/RTU/SimCNV7/services/TransZone35
//http://localhost:3000/RTU/SimCNV8/services/TransZone12
//http://localhost:3000/RTU/SimCNV8/services/TransZone23
//http://localhost:3000/RTU/SimCNV8/services/TransZone35
//http://localhost:3000/RTU/SimCNV9/services/TransZone12
//http://localhost:3000/RTU/SimCNV9/services/TransZone23
//http://localhost:3000/RTU/SimCNV9/services/TransZone35
//http://localhost:3000/RTU/SimCNV10/services/TransZone12
//http://localhost:3000/RTU/SimCNV10/services/TransZone23
//http://localhost:3000/RTU/SimCNV10/services/TransZone35
//http://localhost:3000/RTU/SimCNV11/services/TransZone12
//http://localhost:3000/RTU/SimCNV11/services/TransZone23
//http://localhost:3000/RTU/SimCNV11/services/TransZone35
//http://localhost:3000/RTU/SimCNV12/services/TransZone12
//http://localhost:3000/RTU/SimCNV12/services/TransZone23
//http://localhost:3000/RTU/SimCNV12/services/TransZone35
//http://localhost:3000/RTU/SimCNV1/services/TransZone12
//http://localhost:3000/RTU/SimCNV1/services/TransZone23

//http://localhost:3000/RTU/SimROB1/services/LoadPaper

//http://localhost:3000/RTU/SimCNV1/services/TransZone35
//http://localhost:3000/RTU/SimCNV2/services/TransZone12
//http://localhost:3000/RTU/SimCNV2/services/TransZone23
//http://localhost:3000/RTU/SimROB2/services/Draw1

//http://localhost:3000/RTU/SimCNV2/services/TransZone35
//http://localhost:3000/RTU/SimCNV3/services/TransZone12
//http://localhost:3000/RTU/SimCNV3/services/TransZone23
//http://localhost:3000/RTU/SimROB3/services/ChangePenGREEN
//http://localhost:3000/RTU/SimROB3/services/Draw2

//http://localhost:3000/RTU/SimCNV3/services/TransZone35
//http://localhost:3000/RTU/SimCNV4/services/TransZone12
//http://localhost:3000/RTU/SimCNV4/services/TransZone23
//http://localhost:3000/RTU/SimROB4/services/ChangePenBLUE
//http://localhost:3000/RTU/SimROB4/services/Draw3

//http://localhost:3000/RTU/SimCNV4/services/TransZone35
//http://localhost:3000/RTU/SimCNV5/services/TransZone12
//http://localhost:3000/RTU/SimCNV5/services/TransZone23
//http://localhost:3000/RTU/SimROB5/services/ChangePenBLUE
//http://localhost:3000/RTU/SimROB5/services/Draw4

//http://localhost:3000/RTU/SimCNV5/services/TransZone35
//http://localhost:3000/RTU/SimCNV6/services/TransZone12
//http://localhost:3000/RTU/SimCNV6/services/TransZone23
//http://localhost:3000/RTU/SimROB6/services/ChangePenGREEN
//http://localhost:3000/RTU/SimROB6/services/Draw5

//http://localhost:3000/RTU/SimCNV6/services/TransZone35
//http://localhost:3000/RTU/SimCNV7/services/TransZone12
//http://localhost:3000/RTU/SimCNV7/services/TransZone23

//http://localhost:3000/RTU/SimROB7/services/UnloadPallet


var ww = 0;
var delayInMilliseconds = 4000; //4 second
var i1 = ['SimROB7', 'SimCNV7', 'SimCNV8', 'SimCNV8', 'SimCNV8', 'SimCNV9', 'SimCNV9', 'SimCNV9', 'SimCNV10', 'SimCNV10', 'SimCNV10', 'SimCNV11', 'SimCNV11', 'SimCNV11', 'SimCNV12', 'SimCNV12', 'SimCNV12', 'SimCNV1', 'SimCNV1', 'SimROB1', 'SimCNV1', 'SimCNV2', 'SimCNV2', 'SimROB2', 'SimCNV2', 'SimCNV3', 'SimCNV3', 'SimROB3', 'SimROB3', 'SimCNV3', 'SimCNV4', 'SimCNV4', 'SimROB4', 'SimROB4', 'SimCNV4', 'SimCNV5', 'SimCNV5', 'SimROB5', 'SimROB5', 'SimCNV5', 'SimCNV6', 'SimCNV6', 'SimROB6', 'SimROB6', 'SimCNV6', 'SimCNV7', 'SimCNV7', 'SimROB7'];
var i2 = ['SimROB7', 'SimCNV7', 'SimCNV8', 'SimCNV8', 'SimCNV8', 'SimCNV9', 'SimCNV9', 'SimCNV10', 'SimCNV10', 'SimCNV10', 'SimCNV11', 'SimCNV11', 'SimCNV11', 'SimCNV12', 'SimCNV12', 'SimCNV12', 'SimCNV1', 'SimCNV1', 'SimROB1', 'SimCNV1', 'SimCNV2', 'SimCNV2', 'SimROB2', 'SimCNV2', 'SimCNV3', 'SimCNV3', 'SimROB3', 'SimROB3', 'SimCNV3', 'SimCNV4', 'SimCNV4', 'SimROB4', 'SimROB4', 'SimCNV4', 'SimCNV5', 'SimCNV5', 'SimROB5', 'SimROB5', 'SimCNV5', 'SimCNV6', 'SimCNV6', 'SimROB6', 'SimROB6', 'SimCNV6', 'SimCNV7', 'SimCNV7', 'SimROB7'];
var i3 = ['SimROB7', 'SimCNV7', 'SimCNV8', 'SimCNV8', 'SimCNV9', 'SimCNV9', 'SimCNV10', 'SimCNV10', 'SimCNV11', 'SimCNV11', 'SimCNV11', 'SimCNV12', 'SimCNV12', 'SimCNV12', 'SimCNV1', 'SimCNV1', 'SimROB1', 'SimCNV1', 'SimCNV2', 'SimCNV2', 'SimROB2', 'SimCNV2', 'SimCNV3', 'SimCNV3', 'SimROB3', 'SimROB3', 'SimCNV3', 'SimCNV4', 'SimCNV4', 'SimROB4', 'SimROB4', 'SimCNV4', 'SimCNV5', 'SimCNV5', 'SimROB5', 'SimROB5', 'SimCNV5', 'SimCNV6', 'SimCNV6', 'SimROB6', 'SimROB6', 'SimCNV6', 'SimCNV7', 'SimCNV7', 'SimROB7'];

var j = ['LoadPallet', 'TransZone35', 'TransZone12', 'TransZone23', 'TransZone35', 'TransZone12', 'TransZone23', 'TransZone35', 'TransZone12', 'TransZone23', 'TransZone35', 'TransZone12', 'TransZone23', 'TransZone35', 'TransZone12', 'TransZone23','TransZone35', 'TransZone12', 'TransZone23', 'LoadPaper', 'TransZone35', 'TransZone12', 'TransZone23', 'Draw1', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenGREEN', 'Draw2', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenBLUE', 'Draw2', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenBLUE', 'Draw8', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenGREEN', 'Draw5', 'TransZone35', 'TransZone12', 'TransZone23', 'UnloadPallet'];
var r = ['LoadPallet', 'TransZone35', 'TransZone12', 'TransZone23', 'TransZone35', 'TransZone14', 'TransZone45', 'TransZone12', 'TransZone23', 'TransZone35', 'TransZone12', 'TransZone23', 'TransZone35', 'TransZone12', 'TransZone23','TransZone35', 'TransZone12', 'TransZone23', 'LoadPaper', 'TransZone35', 'TransZone12', 'TransZone23', 'Draw1', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenGREEN', 'Draw2', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenBLUE', 'Draw7', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenBLUE', 'Draw9', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenGREEN', 'Draw5', 'TransZone35', 'TransZone12', 'TransZone23', 'UnloadPallet'];
var q = ['LoadPallet', 'TransZone35', 'TransZone14', 'TransZone45', 'TransZone14', 'TransZone45', 'TransZone14', 'TransZone45', 'TransZone12', 'TransZone23', 'TransZone35', 'TransZone12', 'TransZone23','TransZone35', 'TransZone12', 'TransZone23', 'LoadPaper', 'TransZone35', 'TransZone12', 'TransZone23', 'Draw1', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenGREEN', 'Draw2', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenBLUE', 'Draw4', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenBLUE', 'Draw8', 'TransZone35', 'TransZone12', 'TransZone23', 'ChangePenGREEN', 'Draw5', 'TransZone35', 'TransZone12', 'TransZone23', 'UnloadPallet'];

var fLen = i1.length;

WSs = [];
var ws1 = new ws.WS(1);
WSs.push(ws1);
var ws7 = new ws.WS(7);
WSs.push(ws7);
var ws4 = new ws.WS(4);
WSs.push(ws4);
var ws10 = new ws.WS(10);
WSs.push(ws10);

ws1.subToEvents(5502);
ws7.subToEvents(5508);
ws4.subToEvents(5509);
ws10.subToEvents(5510);

    //your code to be executed after 1 second
    // for (ww = 0; ww < fLen; ww++)
    // {}
io.on('connection', function(client) {
    console.log('Client connected...');
    //when the server receives clicked message, do this
    // Response for Button1 to execute operation1
    client.on('click1', function() {
        setInterval(
            function () {
                var options = {
                    method: 'post',
                    body: 	{"destUrl":"http://localhost:3000/fmw"}, // Javascript object payload
                    json: true,
                    url: ""
                };
                var urlHeadZone = "http://localhost:3000/RTU/";
                var urlTailZone = "/services/";
                options.url = urlHeadZone + i1[ww] + urlTailZone + j[ww];
                request(options, function (error, response, body) {
                    if (error) {
                        console.log('Error :', error);
                        return;
                    }
                    console.log(' Body :', JSON.stringify(body));
                    client.emit('button1', JSON.stringify(body));
                });
                ww = ww+1;
            }, delayInMilliseconds);
        ww = 0;
        client.emit('buttonUpdate');});
        // Response for Button2 to execute operation2
        client.on('click2', function() {
            setInterval(
            function () {
                var options = {
                    method: 'post',
                    body: 	{"destUrl":"http://localhost:3000/fmw"}, // Javascript object payload
                    json: true,
                    url: ""
                };
                var urlHeadZone = "http://localhost:3000/RTU/";
                var urlTailZone = "/services/";
                options.url = urlHeadZone + i2[ww] + urlTailZone + r[ww];
                request(options, function (error, response, body) {
                    if (error) {
                        console.log('Error :', error);
                        return;
                    }
                    console.log(' Body :', JSON.stringify(body));
                    client.emit('button2', JSON.stringify(body));
                });
                ww = ww+1;
            }, delayInMilliseconds);
            ww = 0;
            client.emit('buttonUpdate');});

        // Response for Button2 to execute operation2
    client.on('click3', function() {
        setInterval(
            function () {
                var options = {
                    method: 'post',
                    body: 	{"destUrl":"http://localhost:3000/fmw"}, // Javascript object payload
                    json: true,
                    url: ""
                };
                var urlHeadZone = "http://localhost:3000/RTU/";
                var urlTailZone = "/services/";
                options.url = urlHeadZone + i3[ww] + urlTailZone + q[ww];
                request(options, function (error, response, body) {
                    if (error) {
                        console.log('Error :', error);
                        return;
                    }
                    console.log(' Body :', JSON.stringify(body));
                    client.emit('button3', JSON.stringify(body));
                });
                ww = ww+1;
            }, delayInMilliseconds);
        ww = 0;
        client.emit('buttonUpdate');});

        //send a message to ALL connected clients
        // io.emit('buttonUpdate');
    // notification about the status of workstations
    client.on('workstationbutton', function() {
        setInterval(function(){
            WSs.forEach(function(ws){
                var status = ws.getStatus();
                // console.log(status);
                client.emit('workstation_notify', status);
            });
        }, 3000);
    });
    });

//start our web server and socket.io server listening
server.listen(3333, function(){
    console.log('listening on *:3333');
});
