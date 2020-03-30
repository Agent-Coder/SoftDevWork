//Emily Zhang and Amanda Zheng (Team Me)
//SoftDev1 pd13
//K#13 -- Ask Cricles [Change || Die]
//2020-03-30
var pic = document.getElementById("playground");
var lastx;
var lasty;
var count=0;
var changed=false;
var change = function(num) {
  x=Math.random()*600;
  y=Math.random()*600;
  if(pic.children[num].getAttribute("fill")=="cyan"){
    pic.children[num].setAttribute("cx",x);
    pic.children[num].setAttribute("cy",y);
    pic.children[num].setAttribute("stroke","blue");
    pic.children[num].setAttribute("fill","blue");
  }else{
    pic.children[num].setAttribute("stroke","cyan");
    pic.children[num].setAttribute("fill","cyan");
  }
  changed=true;
}
var clear = function(){
  while(pic.firstChild){
      pic.removeChild(pic.firstChild);
  }
  lastx=null;
  lasty=null;
}


pic.addEventListener('mousedown', e => {
  var x = e.offsetX;
  var y = e.offsetY;
  var circ= document.createElementNS("http://www.w3.org/2000/svg","circle");
  if(!changed){
    circ.setAttribute("cx",x);
    circ.setAttribute("cy",y);
    circ.setAttribute("r",25);
    circ.setAttribute("fill","blue");
    circ.setAttribute("id",count);
    circ.setAttribute("stroke","blue");
    circ.setAttribute("onmousedown","change("+circ.getAttribute("id")+")");
    pic.appendChild(circ);
    count++;
  }
  changed=false;
  lastx=e.offsetX;
  lasty=e.offsetY;
});

var clearbtn = document.getElementById("clear");
clearbtn.addEventListener('click', clear);
