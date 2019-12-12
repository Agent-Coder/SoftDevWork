//Jackie Lin and Amanda Zheng (Team DJAJ)
//SoftDev1 pd1
//K#29 -- Sequential Progression III
//2019-12-12

var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e.srcElement.innerHTML;
};

var removeItem = function(e) {
  e.srcElement.remove();
};

//helper function for adding event listeners to a list item
var addEvents = function(element) {
  element.addEventListener('mouseover', changeHeading);
  element.addEventListener('mouseout', () => {
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!";
  });
  element.addEventListener('click', removeItem);
}

var lis = document.getElementsByTagName("li");
//console.log(lis);

for (var i=0; i < lis.length; i++){
  addEvents(lis[i]);
}

var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  addEvents(item);
  list.appendChild(item);
  lis = document.getElementsByTagName("li");
  //console.log(lis);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
  if (n < 2) return 1;
  return fib(n - 1) + fib(n - 2);
}

var addFib = function(e) {
  console.log(e);
  var fiblist = document.getElementById("fiblist");
  var n = fiblist.getElementsByTagName("li").length;
  //console.log(fib(2));
  var item = document.createElement("li");
  item.innerHTML = fib(n);
  fiblist.appendChild(item);
};

var countfib = 0;
var fibarray = [0, 1, 1];

var fib2 = function(n){
  if (fibarray[n]){
    return fibarray[n];
  }
  fibarray.push(fibarray[n-1] + fibarray[n-2]);
  //console.log(fibarray);
  return fibarray[n];
};

var addFib2 = function(e) {
  countfib++;
  var fiblist=document.getElementById("fiblist");
  var item = document.createElement("li");
  var calculate=fib2(countfib);
  item.innerHTML = calculate;
  fiblist.appendChild(item);
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib2);
