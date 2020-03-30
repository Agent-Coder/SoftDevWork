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
    for (var i = num+1; i < pic.children.length; i++) {
      pic.children[i].setAttribute("id",pic.children[i].getAttribute("id")-1);
      pic.children[i].setAttribute("onmousedown","change("+pic.children[i].getAttribute("id")+")");
    }
    pic.removeChild(pic.children[num])
    var circ= document.createElementNS("http://www.w3.org/2000/svg","circle");
    circ.setAttribute("cx",x);
    circ.setAttribute("cy",y);
    circ.setAttribute("r",25);
    circ.setAttribute("fill","blue");
    circ.setAttribute("id",count-1);
    circ.setAttribute("stroke","blue");
    circ.setAttribute("onmousedown","change("+circ.getAttribute("id")+")");
    pic.appendChild(circ);
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
