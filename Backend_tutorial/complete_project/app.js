const express = require("express");
const bodyParser = require("body-parser");
const { static } = require("express");
const { json } = require("body-parser");
const app = express();
// This line to use EJS template for rendering the HTML pages
let item = "";
let WorkItems=[];
let professions = ["FullStackDeveloper", "RoboticsEngineer"];
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static("public"));  // this command to serve the css and other sheets inside the public folder

    let today = new Date();
    let options = {
      weekday: "long",
      day: "numeric",
      month: "long",
    };
    let day = today.toLocaleDateString("en-US", options);
    // var currentDay = today.getDay();
    // var dayname = "";
    // switch (currentDay) {
    //   case 0:
    //     dayname = "sunday";
    //     break;
    //   case 1:
    //     dayname = "monday";
    //     break;
    //   case 2:
    //     dayname = "tuesday";
    //     break;
    //   case 3:
    //     dayname = "wednesday";
    //     break;
    //   case 4:
    //     dayname = "thursday";
    //     break;
    //   case 5:
    //     dayname = "friday";
    //     break;
    //   case 6:
    //     dayname = "saturday";
    //     break;
    //   default:
    //     console.log("Non-recognizable day");
    //     break;
    // }

app.get("/", function(req,res){
    // console.log(today, currentDay);
    // // currentDay = 0;
    // if (currentDay===0 || currentDay===6){
    //     res.send("<h1>It is weekend :))</h1>");
    // }else{
    //     res.send("<h1>It is working day :((</h1>");
    // }
    // dayName is the variable to be substituted in lists.ejs
    res.render("lists", { ListTitle: day, NewListItem: professions });
});
app.post("/",function(req,res){
    item = req.body.newItem;
    // console.log(req.body)
    if (req.body.list==="Candidates") {
        WorkItems.push(item);
        res.redirect("/work");
    }else{
        professions.push(item);
        res.redirect("/");
    }

});
app.get("/work", function(req,res){
    res.render("lists", { ListTitle: "Candidates", NewListItem: WorkItems });
});
app.post("/work", function(req,res){
    let item = req.body.newItem;
    WorkItems.push(item);
    res.redirect("/work");
})
app.listen(3000, function(){
    console.log("server is running on port 3000");
});