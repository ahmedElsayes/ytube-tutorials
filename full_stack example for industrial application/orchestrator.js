/**
 * Created by Andrei Lobov.
 *
 * The orchestrator
 */

const http = require('http');
const request = require('request');


var optionsCntrl = {
    method: 'post',
    body: {"destUrl":"http://localhost:fmw"}, // Javascript object payload
    json: true,
    url: "http://localhost:3000/RTU/SimROB7/services/LoadPallet",
    headers: {
        'Content-Type': 'application/json'
    }
};
