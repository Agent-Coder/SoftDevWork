//Amanda Zheng and Yevgeniy Gorbachev
//Softdev pd 1
//K28 --  Sequential Progression II: Electric Boogaloo...
//12-11-2019
var funct="fact";
document.getElementById('fact').addEventListener("click", () => getBoxes("fact"));
document.getElementById('fib').addEventListener("click", () => getBoxes("fib"));
document.getElementById('gcd').addEventListener("click", () =>  getBoxes("gcd"));
document.getElementById('selectRandom').addEventListener("click", () => getBoxes("selectRandom"));
const button2= document.getElementById('calculate');
button2.addEventListener("click", () => getFunction());

var fact = function(n){
    if(n <= 1){
      return 1;
    }
    return n*fact(n-1);
};

var fibarray = [0,1,1];
var fib = function(n){
    if(n==0){
      return 0;
    }
    if (fibarray[n]){
      return fibarray[n];
    }
    fibarray[n] = fib(n-1) + fib(n-2);
    return fibarray[n];
};

var gcd = function(a,b){
    if(a % b == 0){
      return b;
    }
    return gcd(b, a % b);
};

var selectRandom = function(array){
    return array[Math.floor(Math.random()*array.length)];
};

var getBoxes = function(chosen){
  document.getElementById("demo").innerHTML="";
  if (chosen=="fact"){
    document.getElementById("box1").innerHTML="Calculate Factorial of: ";
    document.getElementById("b1").style.display = "block";
    document.getElementById("box2").innerHTML="";
    document.getElementById("b2").style.display = "none";
    funct="fact";
    //document.getElementById('calculate').addEventListener("click", getFunction);
  }else if(chosen=="fib"){
    document.getElementById("box1").innerHTML="Find the kth number of Fibonacci number where k is: ";
    document.getElementById("b1").style.display = "block";
    document.getElementById("box2").innerHTML="";
    document.getElementById("b2").style.display = "none";
    funct="fib";
  }else if(chosen=="gcd"){
    document.getElementById("box1").innerHTML="First number: ";
    document.getElementById("b1").style.display = "block";
    document.getElementById("box2").innerHTML="Second number: ";
    document.getElementById("b2").style.display = "block";
    funct="gcd";
  }else{
    document.getElementById("box1").innerHTML="Give a List separated by commas:";
    document.getElementById("b1").value = "a,b,c,d";
    document.getElementById("b1").style.display = "block";
    document.getElementById("box2").innerHTML="";
    document.getElementById("b2").style.display = "none";
    funct="selectRandom";
  }
  document.getElementById("calculate").style.display = "block";
};
var getFunction = function(){
  var ans1=document.getElementById("b1").value;
  var ans2=document.getElementById("b2").value;
  ans1=parseInt(ans1);
  ans2=parseInt(ans2);
  document.getElementById("demo").style.color="black";
  if (funct=="fact" && Number.isInteger(ans1) && ans1>=0){
    console.log("Factorial of "+ans1+": "+fact(ans1));
    return document.getElementById("demo").innerHTML="Your answer: "+fact(ans1);
  }else if(funct=="fib"  && Number.isInteger(ans1) && ans1>=0){
    console.log("Fibonacci "+ans1+": "+fib(ans1));
    return document.getElementById("demo").innerHTML="Your answer: "+fib(ans1);
  }else if(funct=="gcd"  && Number.isInteger(ans1) && ans1>0  && Number.isInteger(ans2) && ans2>0 ){
    console.log("GCD of ("+ans1+","+ans2+"): "+gcd(ans1,ans2));
    return document.getElementById("demo").innerHTML="Your answer: "+gcd(ans1,ans2);
  }else if(funct=="selectRandom"){
    ans1=document.getElementById("b1").value.split(",");
    var rand=selectRandom(ans1);
    console.log("Randomly Generating Element From List ["+ans1+"]: "+rand);
    return document.getElementById("demo").innerHTML="Your answer: "+rand;
  }
  console.log("Error")
  document.getElementById("demo").style.color="red";
  document.getElementById("demo").innerHTML="Please fill out all fields correctly";
};
