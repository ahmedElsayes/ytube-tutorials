//COP - three classes demonstration Customer, Order and Product
//AnLo, 29.09.

var products = require("./Product.js");
var orders = require("./Order.js");
var customers = require("./Customer");

var http = require("http");
//var opcua = require("node-opcua");




var product1 = new products.Product(123, "Blue jeans", 138);
var product2 = new products.Product(124, "Shirt", 23);
var product3 = new products.Product(125, "Cup", 7.5);

var order1 = new orders.Order(231);
order1.addProduct(product1);
order1.addProduct(product2);

var order2 = new orders.Order(232);
order2.addProduct(product3);

var customer = new customers.Customer("John Smith");
customer.addNewOrder(order1);
customer.addNewOrder(order2);

console.log(customer.getCustomerInfo());

var myServer = http.createServer(function(req, res){
    console.log("Method: ", req.method);
    var url = req.url;

    if(req.method == "GET" && url == "/orders"){
        res.setHeader('Content-Type', "text/html");
        res.write("<html><body><p>" + customer.getCustomerInfo() + "</p></body></html>");
        res.end();
    } else {
        res.setHeader('Content-Type', "text/html");
        res.write("<html><body><p>Waiting for correct URL</p></body></html>");
        res.end();
    }
});

myServer.listen(1234, "127.0.0.1", function(){
    console.log("Server is running...");
});