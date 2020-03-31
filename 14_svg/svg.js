//Jackie Lin and Amanda Zheng (Team DJAJ)
//SoftDev1 pd1
//K#14 -- Change || Die While Moving
//2020-04-01

var pic = document.getElementById("vimage");
var clearbtn = document.getElementById("clear");
var movebtn = document.getElementById("move");
var xtrabtn = document.getElementById("xtra");
var id = 0;

var clear = function(){
  while (pic.firstChild){
    pic.removeChild(pic.firstChild);
  }
  window.cancelAnimationFrame(id);
  id = 0;
}

var move = function(){
  window.cancelAnimationFrame(id);
  id = 0;
  id = window.requestAnimationFrame(float);
}

var float = function(e){
  for (i = 0; i < pic.children.length; i++){
    var circle = pic.children[i];
    var cx = parseInt(circle.getAttribute("cx"));
    var cy = parseInt(circle.getAttribute("cy"));
    if (cx >= 480){
      circle.setAttribute("inc_x", -1);
    }
    else if (cx <= 20){
      circle.setAttribute("inc_x", 1);
    }
    if (cy >= 480){
      circle.setAttribute("inc_y", -1);
    }
    else if (cy <= 20){
      circle.setAttribute("inc_y", 1);
    }
    var inc_x = parseInt(circle.getAttribute("inc_x"));
    var inc_y = parseInt(circle.getAttribute("inc_y"));
    circle.setAttribute("cx", cx + inc_x);
    circle.setAttribute("cy", cy + inc_y);
  }
  if (id != 0) {
    id = window.requestAnimationFrame(float);
  }
}

var xtra = function(){
  window.cancelAnimationFrame(id);
  id = window.requestAnimationFrame(changespeed);
}

var changespeed = function(){
  for (i = 0; i < pic.children.length; i++){
    var circle = pic.children[i];
    var cx = parseInt(circle.getAttribute("cx"));
    var cy = parseInt(circle.getAttribute("cy"));
    inc_x = 0;
    inc_y = 0;
    while (inc_x==0 || inc_y==0){
      console.log("yes");
      inc_x = Math.floor(Math.random() * 10 - 5);
      inc_y = Math.floor(Math.random() * 10 - 5);
    }
    circle.setAttribute("inc_x", inc_x);
    circle.setAttribute("inc_y", inc_y);
    circle.setAttribute("cx", cx + inc_x);
    circle.setAttribute("cy", cy + inc_y);
  }
  if (id != 0) {
    id = window.requestAnimationFrame(float);
  }
}

var createcircle = function(e){
  if (e.target == pic){ //blank canvas
    var x = e.offsetX;
    var y = e.offsetY;

    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", 20);
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "blue");
    c.setAttribute("inc_x", 1);
    c.setAttribute("inc_y", 1);
    c.addEventListener('click', changecircle);
    pic.appendChild(c);
  }
}

var changecircle = function(e){ //clicking on circle
  if (e.target.getAttribute("fill") == "blue"){
    e.target.setAttribute("fill", "cyan");
    e.target.setAttribute("stroke", "cyan");
  }
  else{
    var x = Math.floor(Math.random() * 500);
    var y = Math.floor(Math.random() * 500);
    e.target.setAttribute("cx", x);
    e.target.setAttribute("cy", y);
    e.target.setAttribute("fill", "blue");
    e.target.setAttribute("stroke", "blue");
  }
}

pic.addEventListener('click', createcircle);
clearbtn.addEventListener('click', clear);
movebtn.addEventListener('click', move);
xtrabtn.addEventListener('click', xtra);
