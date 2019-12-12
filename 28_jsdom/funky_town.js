//Amanda Zheng and Yvgeniy Gorbachev
//Softdev pd 1
//K27 -- Sequential Progression
//12-11-2019
const button = document.getElementById('b');
console.log("Button", button);
button.addEventListener("click", () => getBoxes());
if(document.getElementById("calculate").style.visibility=="visible"){
  console.log("yeet");
  document.getElementById('calculate').addEventListener("click", getFunction);
}
console.log("calculate", document.getElementById("calculate"));
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
    document.getElementById("box1").innerHTML="Calculate Factorial of: <input type=\"text\" name=\"box1\" value=5><br>";
    //document.getElementById('calculate').addEventListener("click", getFunction);
  }else if(chosen=="fib"){
    document.getElementById("box1").innerHTML="Find the kth number of Fibonacci number where k is: <input type=\"text\" name=\"box1\" value=5><br>";
  }else if(chosen=="gcd"){
    document.getElementById("box1").innerHTML="First number: <input type=\"text\" name=\"box1\" value=5><br>";
    document.getElementById("box2").innerHTML="Second number: <input type=\"text\" name=\"box1\" value=10><br>";
  }else{
    document.getElementById("box1").innerHTML="Give a List separated by commas: <input type=\"text\" name=\"box1\" value=\"Amanda,Yvgeniy,Mandy,Pratham\"><br>";
  }
  console.log(document.getElementById("calculate").style.visibility);
  document.getElementById("calculate").style.visibility = "visible";
  console.log(document.getElementById("calculate").style.visibility);
  //document.getElementById('calculate').addEventListener("click", getFunction);
};
var getFunction = function(){
  var funct=document.getElementById('select_method').options[document.getElementById('select_method').selectedIndex].value;
  var ans1=document.getElementById("box1").value;
  if (funct=="fact"){
    return document.getElementById("demo").innerHTML="Your answer: "+fact(ans1);
  }else if(funct=="fib"){
    return document.getElementById("demo").innerHTML="Your answer: "+fib(ans1);
  }else if(funct=="gcd"){
    var ans2=document.getElementById("box2").value;
    return document.getElementById("demo").innerHTML="Your answer: "+gcd(ans1,ans2);
  }else if(funct=="selectRandom"){
    ans1=str.split(",");
    return document.getElementById("demo").innerHTML="Your answer: "+selectRandom(ans1);
  }
  return document.getElementById("demo").innerHTML="Please put in stuff";
};
