
var nameList=["ahmed","ali","islam","hassan","twfik"];
function whosPaying(names) {
    var i = Math.floor(names.length * Math.random());
    var selected = names[i];
    var result = selected + " is going to buy lunch today!";
    return result;
}
console.log(whosPaying(nameList));