/**
 * Created by Andrei Lobov.
 *
 * The gateway to call the RESTful services.
 *
 * To be RUN as NODE.JS file.
 *
 */

const http = require('http');
const request = require('request');
const gatewayHost = '127.0.0.1'; //The local host IP.
const gatewayPort = 4590;

//Forming the parameters for the request as a JSON
//This structure will be used and updated to form valid call - url and body will be replaced.
var options = {
    method: 'post',
    body: {"destUrl":"http://localhost:fmw"}, // Javascript object payload
    json: true,
    url: "http://localhost:3000/RTU/SimROB7/services/LoadPallet",
    headers: {
        'Content-Type': 'application/json'
    }
};

/**
 *
 * @param data - has the following format
 * { url: <the url of the service>,
 *   payload: <the payload message to POST to the service of the url>
 * }
 * @param res - where to send response
 */
function callRESTService(data, res){

    //Getting and updating the data for the further request
    var url = data.url;
    console.log("url:" + url); //Just prining out the URL to be invoked.
    var payload = data.payload;
    var type = data.type;

    options.url = url;
    options.body = payload;
    options.headers = {'Content-Type' : type};

    //Forward further the HTTP POST request AND return the result to the orginal source of the request.
    request(options, function (err, res2, body) {
        if (err) {
            console.log('Error :', err);
            return;
        }
        console.log(' Body :', body);

        //Note, using the res object passed to the callRESTService method. So, the gateway will sent back the result of operation.
        res.statusCode = 200;
        res.setHeader('Access-Control-Allow-Origin', '*');
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify(body));
    });

}

const gatewayServer = http.createServer(function(req, res) {
    var method = req.method;
    //console.log(..your message..) - can be used in many places for the debugging peurposes.
    console.log("Method: " + method);

    if(method == 'OPTIONS'){
        //Handling "preflight"
        //First the client will ask about the options:
        //http://zacstewart.com/2012/04/14/http-options-method.html
        res.statusCode = 200;
        res.setHeader('Allow', 'GET,POST,OPTIONS');
        res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
        res.setHeader('Access-Control-Allow-Origin', '*'); //Allowing cross domain/origin calls! https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
        // res.setHeader('Content-Type', 'application/json');
        res.end('OK');
    }
    else if(method == 'GET'){
        //Handle GET method.
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Server is operational.\nUse HTTP POST to invoke its operations. The payload should be as follows: \n{ url: <the url of the service>,\n' +
            'payload: <the payload message to POST to the service of the url>}');
    } else if(method == 'POST'){
        //Handle POST method.
        var body = []; //Getting data: https://nodejs.org/en/docs/guides/anatomy-of-an-http-transaction/
        req.on('data', function(chunk) {
            body.push(chunk);
            var abc = JSON.parse(body.toString());
            var result = callRESTService(abc, res);

        });

    }
});

gatewayServer.listen(gatewayPort, gatewayHost, () => {
    console.log(`Gateway server is running at http://${gatewayHost}:${gatewayPort}/`);
});

