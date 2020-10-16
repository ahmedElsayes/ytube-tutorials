// functions in typescript
function App(user :string){
    return  "Hello " + user;  // This just to enshur that whatever i type will be string
}
let myname = "Ahmed";
let num = prompt("Please enter a number");
// let testnum = parseInt(num);
// let myname = prompt("Please enter your name");

document.getElementById("zero").innerHTML = num;
document.getElementById("first").innerHTML = App(myname);
// to learn about interface in typescript
// passing an object to the function
interface person {
    firstname: string;
    secondname: string;
}

function Proname(someone:person){
    return "Hello " + someone.firstname + " " +someone.secondname;
}
let hisname = {firstname: "Ahmed", secondname: "Elsayes"};
document.getElementById("second").innerHTML = Proname(hisname);

// example of working with classes in typescript
class scholar{
    fullname: string;
    email: string; 
    constructor(firstname:string, secondname:string){
        this.fullname = firstname + " " + secondname;
        this.email = firstname+"."+secondname+"@gmail.com";
    }
    //defining a method
    task(){
        return this.fullname + " studies anything";
    }
}
// example of creating a subclass that inherites
class student extends scholar{
    material: string[];
    constructor(firstname: string, secondname: string, material:string[]){
        super(firstname,secondname);
        this.material = material;
    }
    task(){
        return this.fullname + " studies " + this.material.map(subItem => {return " " +subItem});
    }
}
let person1 = new scholar("hazem", "abdelrahman");
let person2 = new student("hassan", "Elsayes", ["Automation","software","cyberSecurity"]);
document.getElementById("third").innerHTML = person1.task();
document.getElementById("forth").innerHTML = person2.task();
