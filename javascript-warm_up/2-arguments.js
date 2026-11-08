#!/usr/bin/node

let countThewords = process.argv.length - 2;

if(countThewords === 0){
    console.log("No argument");
}else{
    console.log("Argument found")
}