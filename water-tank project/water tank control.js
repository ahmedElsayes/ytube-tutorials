// This is Javascript code to control water level in a tank
// to make it functional, google on npm water-tank and follow the instructions to install the module
// copy rights of this code returns to the creator of Water-tank module
var Tank = require('water-tank');
var tank1 = new Tank(10, 2.5, 1, 0.013, 0.7, 0.60, 3001);
tank1.on('HIGH_LEVEL', function (message) {
    tank1.setValve(1);
});
tank1.on('LOW_LEVEL', function (message) {
    tank1.setValve(0);
});
setTimeout(function () {
    tank1.startExperiment()
}, 3000);