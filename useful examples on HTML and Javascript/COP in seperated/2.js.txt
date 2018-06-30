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

exports.Order = Order;