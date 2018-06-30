//COP - three classes demonstration Customer, Order and Product
//AnLo, 18.09.

//Class Customer definition begins
// Constructor
function Customer(_name) {
    // always initialize all instance properties
    this._name = _name;
    this.orders = []; // default value
}
// class methods
Customer.prototype.addNewOrder = function(order) {
    this.orders.push(order);
};

Customer.prototype.getCustomerInfo = function() {
    //TODO
    var result = 'Customer ' + this._name + ' has ordered:\n';
    for(var i = 0; i<this.orders.length; i++){
        result = result + 'Order: ' + this.orders[i].getOrderInfo() + '.\n';
    }
    return result;
};

//End of Customer class definition

// Constructor for Order class
function Order(orderNum) {
    // always initialize all instance properties
    this.orderNum = orderNum;
    this.products = []; // default value
}
// class methods
Order.prototype.addProduct = function(product) {
    this.products.push(product);
};

Order.prototype.getOrderInfo = function() {
    //TODO
    var result = '';
    for(var i = 0; i<this.products.length; i++){
        result = result + 'Product: ' + this.products[i].getDescription() + ' for ' + this.products[i].getPrice() + ' EUR.\n'
    }
    return result;
};

//End of Order class

// Constructor for Product class
function Product(productNum, description, price) {
    // always initialize all instance properties
    this.productNum = productNum;
    this.description = description;
    this.price = price;
}
// class methods
Product.prototype.getPrice = function() {
    return this.price;
};

Product.prototype.getDescription = function() {
    return this.description;
};

var product1 = new Product(123, "Blue jeans", 138);
var product2 = new Product(124, "Shirt", 23);
var product3 = new Product(125, "Cup", 7.5);

var order1 = new Order(231);
order1.addProduct(product1);
order1.addProduct(product2);

var order2 = new Order(232);
order2.addProduct(product3);

var customer = new Customer("John Smith");
customer.addNewOrder(order1);
customer.addNewOrder(order2);

console.log(customer.getCustomerInfo());