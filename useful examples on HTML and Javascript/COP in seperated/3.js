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

exports.Customer = Customer;