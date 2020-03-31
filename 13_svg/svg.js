//Emily Zhang and Amanda Zheng (Team Me)
//SoftDev1 pd13
//K#13 -- Ask Cricles [Change || Die]
//2020-03-30
var pic = document.getElementById("playground");
var lastx;
var lasty;
var changed=false;
var change = function(e) {
  if (e.target.getAttribute("fill") == "blue"){
    e.target.setAttribute("fill", "cyan");
    e.target.setAttribute("stroke", "cyan");
  }
  else{
    var x = Math.floor(Math.random() * 600);
    var y = Math.floor(Math.random() * 600);
    e.target.setAttribute("cx", x);
    e.target.setAttribute("cy", y);
    e.target.setAttribute("fill", "blue");
    e.target.setAttribute("stroke", "blue");
  }
  changed=true;
}
var clear = function(){
  while(pic.firstChild){
      pic.removeChild(pic.firstChild);
  }
}


var make = function(e) {
  if(!changed){
    var x = e.offsetX;
    var y = e.offsetY;
    var circ= document.createElementNS("http://www.w3.org/2000/svg","circle");
    circ.setAttribute("cx",x);
    circ.setAttribute("cy",y);
    circ.setAttribute("r",25);
    circ.setAttribute("fill","blue");
    circ.setAttribute("stroke","blue");
    circ.addEventListener('click',change);
    pic.appendChild(circ);
  }
  changed=false;
}


var clearbtn = document.getElementById("clear");
clearbtn.addEventListener('click', clear);
pic.addEventListener('click',make);
