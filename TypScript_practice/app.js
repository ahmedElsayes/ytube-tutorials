var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
// functions in typescript
function App(user) {
    return "Hello " + user.toString(); // This just to enshur that whatever i type will be string
}
var myname = "ahmed";
document.getElementById("first").innerHTML = App(myname);
function Proname(someone) {
    return "Hello " + someone.firstname + " " + someone.secondname;
}
var hisname = { firstname: "Ahmed", secondname: "Elsayes" };
document.getElementById("second").innerHTML = Proname(hisname);
// example of working with classes in typescript
var scholar = /** @class */ (function () {
    function scholar(firstname, secondname) {
        this.fullname = firstname + " " + secondname;
        this.email = firstname + "." + secondname + "@gmail.com";
    }
    //defining a method
    scholar.prototype.task = function () {
        return this.fullname + " studies anything";
    };
    return scholar;
}());
// example of creating a subclass that inherites
var student = /** @class */ (function (_super) {
    __extends(student, _super);
    function student(firstname, secondname, material) {
        var _this = _super.call(this, firstname, secondname) || this;
        _this.material = material;
        return _this;
    }
    student.prototype.task = function () {
        return this.fullname + " studies " + this.material;
    };
    return student;
}(scholar));
var person1 = new scholar("hazem", "abdelrahman");
var person2 = new student("hassan", "Elsayes", "Automation Engineering");
document.getElementById("third").innerHTML = person1.task();
document.getElementById("forth").innerHTML = person2.task();
