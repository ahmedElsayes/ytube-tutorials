
var express = require("express");
var port = 3700;

var opcua = require("node-opcua");
var async = require("async");
var client = new opcua.OPCUAClient();
var endpointUrl = "opc.tcp://" + require("os").hostname() + ":3003/MyLittleServer";

var the_session, the_session2, the_subscription;
var startExperimentStringNodeId, ControllerNodeId, setvalveNodeId, getvalveNodeId, getLevelNodeId;

async.series([
        // step 1 : connect to
        function(callback)  {
            client.connect(endpointUrl,function (err) {
                if(err) {
                    console.log(" cannot connect to endpoint :" , endpointUrl );
                } else {
                    console.log("connected !");
                }
                callback(err);
            });
        },
        // step 2 : createSession
        function(callback1) {
            client.createSession( function(err30,session) {
                if(!err30) {
                    the_session = session;
                    console.log("session created");
                }
                callback1(err30);
            });
            client.createSession( function(err31,session2) {
                if(!err31) {
                    the_session2 = session2;
                    console.log("session created");
                }
                callback1(err31);
            });
        },
        // step 3 : browse
        function(callback2) {
            the_session.browse("RootFolder", function(err,browseResult){
                if(!err) {
                    browseResult.references.forEach(function(reference) {
                        console.log( reference.browseName.toString());
                    });
                }
                callback2(err);
            });
        },
        // Reading variables
        // step 4 : read the water level with read variable   ___   Level
        function(callback3) {
            var nodeToRead = { nodeId: "ns=1;s=water_level", attributeId: opcua.AttributeIds.Value };
            the_session.read(nodeToRead, function(err,dataValue) {
                if (!err) {
                    console.log(" The recent water level = " , dataValue.value.value);
                }
                callback3(err);
            });
        },
        // step 5 : read the valve status with read variable   ___   Valve
        function(callback4) {
            var nodeToRead = { nodeId: "ns=1;s=valv", attributeId: opcua.AttributeIds.Value };
            the_session.read(nodeToRead, function(err,dataValue) {
                if (!err) {
                    console.log(" the status of the valve = " , dataValue.value.value);
                }
                callback4(err);
            });
        },

        // to get node id of object by calling TankController  __ ControllerNodeId
        function (callback5) {
            var path3  = opcua.makeBrowsePath("RootFolder","/Objects/TankController");
            //to get id of tankcontroller
            the_session.translateBrowsePath(path3,function(err3,results3){
                if(!err3){
                    ControllerNodeId = results3.targets[0].targetId;
                    console.log(ControllerNodeId.value);
                }
                callback5(err3);
            });
        },

        //*************************    To get all methods ID     *******************************
        // to get method id of starting experiment   __  startExperiment
        function (callback50) {
            var path4  = opcua.makeBrowsePath(ControllerNodeId,".startExperiment");
            the_session.translateBrowsePath(path4,function(err50,results50){
                if(!err50){
                    startExperimentStringNodeId = results50.targets[0].targetId;
                    console.log(startExperimentStringNodeId.value);}
                callback50(err50);
            });
        },
        // to get method id of setting valve_on   __   setValve
        function (callback49) {
            var path5  = opcua.makeBrowsePath(ControllerNodeId,".setValve");
            the_session.translateBrowsePath(path5,function(err49,results49){
                if(!err49){
                    setvalveNodeId = results49.targets[0].targetId;
                    console.log(setvalveNodeId.value);}
                callback49(err49);
            });
        },
        // to get method id for getting the ratio of valve  __  getValve
        function (callback48) {
            var path6  = opcua.makeBrowsePath(ControllerNodeId,".getValve");
            the_session.translateBrowsePath(path6,function(err48,results48){
                if(!err48){
                    getvalveNodeId = results48.targets[0].targetId;
                    console.log(getvalveNodeId.value);}
                callback48(err48);
            });
        },
        // to get method id for getting the level of water in the Tank  __  getLevel
        function (callback47) {
            var path7  = opcua.makeBrowsePath(ControllerNodeId,".getLevel");
            the_session.translateBrowsePath(path7,function(err47,results47){
                if(!err47){
                    getLevelNodeId = results47.targets[0].targetId;
                    console.log(getLevelNodeId.value);
                    console.log("******assigning nodeId to be used in calling methods are done!!*******");
                }
                callback47(err47);
            });
        },

        //***********************************call all methods************************************
        // to call method of  ___ set valve  __ on server side and set it into operation
        function (callback6) {
            the_session.call({
                    objectId: ControllerNodeId,
                    methodId: setvalveNodeId,
                    inputArguments: [{
                        dataType: opcua.DataType.Float,
                        arrayType: opcua.VariantArrayType.Scalar,
                        value:  0 }
                    ]
                },
                function(err,results){
                    if (!err){
                        console.log("Valve set on", results.statusCode);}
                    callback6(err);
                });
        },
        //to call method of  __  start experiment  __ on server side and set it into operation
        function (callback7) {
            the_session.call({
                    objectId: ControllerNodeId,
                    methodId: startExperimentStringNodeId
                },
                function(err,results){
                    if (!err){
                        console.log("Experiment has started", results.statusCode);}
                    callback7(err);
                });
        },
        // close session
        function(callback20) {
            the_session.close(function(err20){
                if(err20) {
                    console.log("session closed failed ?");
                }
                console.log("session closed");
                callback20();
            });
        }
    ],

    // ************************************The End of Asynchronous steps************
    // *********interval for getting periodically the level of water and the ratio of valve and actuating it to control*********
    function(err21) {
        if (!err21){
            // To call the history data base by defining express & sockets
            var app = express();
            app.use(express.static(__dirname + '/public'));
            var io = require('socket.io').listen(app.listen(port));
            io.sockets.on('connection', function (socket) {
                console.log("socket connected");
            });
            //*********************water_history*******************************************************************
            setInterval(function waterhistory() {
                var level_History = { nodeId: "ns=1;i=1008", attributeId: opcua.AttributeIds.Value };
                the_session2.read(level_History, function(err,HistorydataValue) {
                    if (!err) {
                        io.sockets.emit('message', {
                            value: HistorydataValue.value.value,
                            timestamp: HistorydataValue.serverTimestamp,
                            browseName: "levelRecord"
                        });
                    }
                    else {console.log(err)}
                });
            },100);

            //to call method of  __   get valve __  from server side and set it into operation
            setInterval(function get_valve() {
                the_session2.call({
                        objectId: ControllerNodeId,
                        methodId: getvalveNodeId
                    },
                    function(err8,results8){
                        if (!err8){
                            console.log("get the ratio of valve", results8.outputArguments[0].value);}
                    });
            },500);
            //to call method of ___ get level  ___ from server side and control flow in range between 70 & 60 %
            setInterval(function water_level() {
                the_session2.call({
                        objectId: ControllerNodeId,
                        methodId: getLevelNodeId
                    },
                    function(err9,results9){
                        if (!err9){
                            var ratio_of_waterlevel = 10*results9.outputArguments[0].value;
                            console.log("ratio of water level in tank", ratio_of_waterlevel);}
                            if (ratio_of_waterlevel > 70){
                                the_session2.call({
                                        objectId: ControllerNodeId,
                                        methodId: setvalveNodeId,
                                        inputArguments: [{
                                            dataType: opcua.DataType.Float,
                                            arrayType: opcua.VariantArrayType.Scalar,
                                            value:  1 }
                                        ]
                                    },
                                    function(err,results){
                                        if (!err){
                                            console.log("Valve set on : status of operation", results.statusCode.name);
                                            console.log("*****************Transition********************");
                                        }
                                    });
                            }
                            if (ratio_of_waterlevel < 60.15){
                                the_session2.call({
                                        objectId: ControllerNodeId,
                                        methodId: setvalveNodeId,
                                        inputArguments: [{
                                            dataType: opcua.DataType.Float,
                                            arrayType: opcua.VariantArrayType.Scalar,
                                            value:  0 }
                                        ]
                                    },
                                    function(err,results){
                                        if (!err){
                                            console.log("Valve set off : status of operation", results.statusCode.name);
                                        }
                                    });
                            }
                    });
            },350);


        }
        else {console.log(err21);}
    }
) ;