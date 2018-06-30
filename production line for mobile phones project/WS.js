// Constructor for Workstation class
const request = require('request');

function WS(num) {
    // always initialize all instance properties
    this.num = num;
    this.subServer = null;
    this.palletIdZ1 = -1;
    this.palletIdZ2 = -1;
    this.palletIdZ3 = -1;
    this.palletIdZ4 = -1;
    this.palletIdZ5 = -1;

}
// class methods
WS.prototype.getNumber = function() {
    return this.num;
};

//Getting the status of WS
WS.prototype.getStatus = function() {
    var status = "WS " + this.num + " has the following status:\n";
    status += "Z1: " + ((this.palletIdZ1 == -1)?"Empty":this.palletIdZ1) + "\n";
    status += "Z2: " + ((this.palletIdZ2 == -1)?"Empty":this.palletIdZ2) + "\n";
    status += "Z3: " + ((this.palletIdZ3 == -1)?"Empty":this.palletIdZ3) + "\n";
    status += "Z4: " + ((this.palletIdZ4 == -1)?"Empty":this.palletIdZ4) + "\n";
    status += "Z5: " + ((this.palletIdZ5 == -1)?"Empty":this.palletIdZ5) + "\n";
    return status;
};

// Subscribing to events for the WS
WS.prototype.subToEvents = function(port) {
    var urlHeadZone = "http://localhost:3000/RTU/SimCNV" + this.num + "/events/Z";
    var urlTailZone = "_Changed/notifs";
    //1. Defining message for subscription
    var options = {
        method: 'post',
        body: {"destUrl":"http://127.0.0.1:" + port}, // Javascript object payload
        json: true,
        url: "http://localhost:3000/RTU/SimCNV7/events/Z3_Changed/notifs", //<-- event we subscribe to.
        headers: {
            'Content-Type': 'application/json'
        }
    };

    for(var i = 1; i < 6; i++){
        //2. Sending subscription defined in options.
        options.url = urlHeadZone + i + urlTailZone;
        request(options, function (err, res, body) {
            if (err) {
                console.log('Error :', err);
                return;
            }
            console.log(' Body :', JSON.stringify(body)); // Just printing the return message as we subscribe.

        });
}};

exports.WS = WS;