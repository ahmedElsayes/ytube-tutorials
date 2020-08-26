const sample = [{
    message: "Not possible to open pulsing valve",
    timestamp: "21.11.2019, 10:15",
    functionid: "SALADIN_process",
    sourceid: "V419",
    value: 0,
    unit: "any",
    priority: "warning",
    messagegroup: "Actuator",
    state: "Active"
},
{
    message: "Not possible to switch on vaccum pump",
    timestamp: "22.11.2019, 10:15",
    functionid: "SALADIN_process",
    sourceid: "V440",
    value: 1,
    unit: "any",
    priority: "Alarm",
    messagegroup: "Actuator",
    state: "Active"
},
{
    message: "Not possible to read temperature",
    timestamp: "23.11.2019, 10:15",
    functionid: "SALADIN_process",
    sourceid: "V412",
    value: 2,
    unit: "any",
    priority: "warning",
    messagegroup: "Actuator",
    state: "Active"
},
{
    message: "Not possible to read pressure of IMS",
    timestamp: "24.11.2019, 10:15",
    functionid: "SALADIN_process",
    sourceid: "V415",
    value: 3,
    unit: "any",
    priority: "warning",
    messagegroup: "Actuator",
    state: "Active"
},
{
    message: "Not possible to open ventlation valve",
    timestamp: "25.11.2019, 10:15",
    functionid: "SALADIN_process",
    sourceid: "V500",
    value: 4,
    unit: "any",
    priority: "Alarm",
    messagegroup: "Actuator",
    state: "Active"
}];
let var1 = require('./example-data.json');
let var2 = [1, 5, 8];
let var3 = ["ahmed", "mahmoud", "Ali"];
// let var4 = require('./example2.json');

var alarms = [];
for (let index = 0; index < var1.length; index++) {
    const element = var1[index];
    if (element.priority==="Alarm"){
        alarms.push(element);
        console.log(index + ":  " + element.priority);
    }
}
// var alarms = [];
// sample.map((instance,indx) => {
//     if (instance.priority === "Alarm"){
//         alarms.push(instance);
//         console.log(indx+":  "+instance.priority);
//     }
// })
// console.log(alarms.length);
// console.log("the reading of first object from JSON file: ",var1[0].priority);
// console.log("JSON file: "+ typeof var1[0].priority, "//object inside the file: "+ typeof sample[0].value);
// console.log("type of var2: "+typeof var2+"   //type of var3: "+typeof var3[1]);
// var alarmsstr = JSON.stringify(alarms);
// console.log(alarmsstr);
