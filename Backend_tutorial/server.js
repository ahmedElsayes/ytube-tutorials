const express = require("express");
const app = express();

app.get("/", function(req,res){
    res.send("Hello Ahmed, Your first web App")
})

app.get('/contact',function(req,res){
    res.send("contact me at ahmed.sayes@outlook.com")
})

app.get('/values',function(req,res){
    res.send("my values: insistance, persistance, temperance")
})
app.listen(3000,function(){
    console.log("server is running on port 3000")
})