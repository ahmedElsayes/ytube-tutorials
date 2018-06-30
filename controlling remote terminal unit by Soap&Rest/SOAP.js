var http = require('http');
const request = require('request');
var express = require("express");
var bodyparser = require("body-parser");
var events = require('events');
var BitArray = require('node-bitarray');
var fs = require ('fs');
// var hbs = require ('hbs');
var eventEmitter = new events.EventEmitter();
app = express();
app.use(bodyparser.json());
// app.use(bodyparser());
// app.get('/', function (req,res){res.send("Hello world");});

app.post('/', function (req,res){
    eventEmitter.emit('submit', req.body);
    res.send("Hello world");
    // console.log(req.body);
});
var options = {
    method: 'post',
    body: 	{"destUrl":"http://localhost:3000"}, // Javascript object payload
    json: true,
    url: "http://192.168.100.103/rest/services/startEvents"};
request(options, function (err, res, body) {
    if (err) {
        console.log('Error :', err);
    }
});
eventEmitter.on('submit', function(msg){
    var ff = new Date();
    var sec = ff.getSeconds();
    var binaries = sec.toString(2);
    var oo = BitArray.parse(sec);
    console.log(oo, sec);
    var invoke = {
        method: 'post',
        url: "http://192.168.100.103:80/dpws/WS01",
        body: '<?xml version="1.0" encoding="ISO-8859-1"?>\n' +
        '<s12:Envelope\n' +
        '        xmlns:s12="http://www.w3.org/2003/05/soap-envelope"\n' +
        '        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">\n' +
        '    <s12:Header>\n' +
        '        <wsa:Action>http://www.tut.fi/fast/Assignment/UpdateOutputs_Request</wsa:Action>\n' +
        '    </s12:Header>\n' +
        '    <s12:Body>\n' +
        '        <Outputs xmlns="http://www.tut.fi/fast/Assignment">\n' +
        '            <output0 xmlns="http://www.tut.fi/fast/Assignment">'+Boolean(oo[0])+'</output0>\n' +
            '            <output1 xmlns="http://www.tut.fi/fast/Assignment">'+Boolean(oo[1])+'</output1>\n' +
            '            <output2 xmlns="http://www.tut.fi/fast/Assignment">'+Boolean(oo[2])+'</output2>\n' +
            '            <output3 xmlns="http://www.tut.fi/fast/Assignment">'+Boolean(oo[3])+'</output3>\n' +
            '            <output4 xmlns="http://www.tut.fi/fast/Assignment">'+Boolean(oo[4])+'</output4>\n' +
            '            <output5 xmlns="http://www.tut.fi/fast/Assignment">'+Boolean(oo[5])+'</output5>\n' +
            '            <output6 xmlns="http://www.tut.fi/fast/Assignment">'+Boolean(oo[6])+'</output6>\n' +
            '            <output7 xmlns="http://www.tut.fi/fast/Assignment">'+Boolean(oo[7])+'</output7>\n' +
            '        </Outputs>\n' +
            '    </s12:Body>\n' +
            '</s12:Envelope>', // Javascript object payload
        headers: {
            'accept-encoding': 'none',
            'accept-charset': 'utf-8',
            'connection': 'close',
            'host': '192.168.100.103:80',
            'content-type': {'accept':'text/xml',
                             'accept':'text/html',
                             'accept':'application/xml'
            }
        }
    };
    // The following code to activate the outputs of the controller
    request(invoke, function (error, response, body) {
        if (error){console.log("Error: ", error);
        // return;
            //Writing output to the designated area
        }
    });
});
app.listen(3000, function (){
    console.log("app running on port localhost:3000");});
// exports.body = Body;