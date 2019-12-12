//Amanda Zheng and Yvgeniy Gorbachev
//Softdev pd 1
//K27 -- Sequential Progression
//12-11-2019
const button = document.getElementById('b');
button.addEventListener("click", () => getBoxes());
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

var getBoxes = function(){
  var funct=document.getElementById('select_method');
  var chosen=funct.options[funct.selectedIndex].value;
  console.log(chosen);
  if (chosen=="fact"){
    document.getElementById("box1").innerHTML="Calculate Factorial of: ";
    document.getElementById("b1").style.display = "block";
    //document.getElementById('calculate').addEventListener("click", getFunction);
  }else if(chosen=="fib"){
    document.getElementById("box1").innerHTML="Find the kth number of Fibonacci number where k is: ";
    document.getElementById("b1").style.display = "block";
  }else if(chosen=="gcd"){
    document.getElementById("box1").innerHTML="First number: ";
    document.getElementById("b1").style.display = "block";
    document.getElementById("box2").innerHTML="Second number: ";
    document.getElementById("b2").style.display = "block";
  }else{
    document.getElementById("box1").innerHTML="Give a List separated by commas: <input type=\"text\" name=\"box1\" value=\"Amanda,Yvgeniy,Mandy,Pratham\"><br>";
    document.getElementById("b1").value = "a,b,c,d";
    document.getElementById("b1").style.display = "block";
  }
  console.log(document.getElementById("calculate").style.display);
  document.getElementById("calculate").style.display = "block";
  console.log(document.getElementById("calculate").style.display);
};
var getFunction = function(){
  var funct=document.getElementById('select_method').options[document.getElementById('select_method').selectedIndex].value;
  console.log(funct);
  var ans1=document.getElementById("b1").text;
  console.log(ans1);
  if (funct=="fact"){
    return document.getElementById("demo").innerHTML="Your answer: "+fact(ans1);
  }else if(funct=="fib"){
    return document.getElementById("demo").innerHTML="Your answer: "+fib(ans1);
  }else if(funct=="gcd"){
    var ans2=document.getElementById("b2").value;
    return document.getElementById("demo").innerHTML="Your answer: "+gcd(ans1,ans2);
  }else if(funct=="selectRandom"){
    ans1=str.split(",");
    return document.getElementById("demo").innerHTML="Your answer: "+selectRandom(ans1);
  }
  return document.getElementById("demo").innerHTML="Please put in stuff";
};
