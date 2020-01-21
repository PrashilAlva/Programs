const express=require('express');
const app=express();

const PORT=8080;

app.get("/",(req,res)=>{
    console.log("Response Processing...");
    res.sendFile(__dirname+"/hello.html");
});

app.listen(PORT,()=>{
    console.log("Request received");
});

