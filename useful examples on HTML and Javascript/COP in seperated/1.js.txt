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

exports.Product = Product;