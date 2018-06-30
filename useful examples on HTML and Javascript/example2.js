console.log("Hello World!");
var abc = "ABC";
var cba = 2.5;

var parts = ["frame", "screen", "keyboard"];
var colors = ["red", "green", "blue"];

console.log(abc+":"+cba);

var x = 5;
var y = 2;
console.log(abc+(x+y));

//Functions declaration
function sum(a1, a2){
    var result = a1 + a2;
    return result;
}
function lightPosition(light){
    if(light != "yellow" && light != "green"){
        return 1;
    } else if(light == "yellow") {
        return 2;
    } else if(light == "green") {
        return 3;
    }
    return "Not known";
}

function displayCustomerChoices(){
    var result = "";
    var coloredProducts = [];
    for(var i = 0; i < parts.length; i++){
        var coloredProduct = [];
        for(var j = 0; j < colors.length; j++){
            result = result + "\n" + parts[i] + " of color " + colors[j];
            coloredProduct.push(parts[i] + " of color " + colors[j]);
        }
        coloredProducts.push(coloredProduct);
    }
    console.log("Products:", coloredProducts);
    return result;
}

/**
 * a function receiving an element, a set from where to pick up next elements.
 * returns all possible combination.
 */

function pickupall()
//Let's use our function
console.log(sum(231, 44523));
console.log(sum("A", "B"));

console.log(lightPosition("yellow"));
console.log(lightPosition("red"));
console.log(lightPosition("asdas")) // ->1

console.log(displayCustomerChoices());