//Emily Zhang and Amanda Zheng (Team Me)
//SoftDev1 pd1
//K#12 -- SVG-DOT
//2020-03-27

var pic = document.getElementById("playground");
var lastx;
var lasty;
var clear = function(){
  //ctx.clearRect(0, 0, c.width, c.height);
  console.log(pic)
  while(pic.firstChild){
      pic.removeChild(pic.firstChild);
  }
  //length=pic.children.length
  //for (let i = length; i > 0; i--) {
    //pic.removeChild(pic.children[pic.children.length-1]);
//  } this method also works!!!!
  lastx=null;
  lasty=null;
  //console.log("clear");
}


pic.addEventListener('mousedown', e => {
  var x = e.offsetX;
  var y = e.offsetY;
  var circ= document.createElementNS("http://www.w3.org/2000/svg","circle");
  circ.setAttribute("cx",x);
  circ.setAttribute("cy",y);
  circ.setAttribute("r",10);
  circ.setAttribute("fill","black");
  circ.setAttribute("stroke","black");
  pic.appendChild(circ);
  if(lastx!=null){
    console.log("yes")
    var line= document.createElementNS("http://www.w3.org/2000/svg","line");
    line.setAttribute("x1", lastx)
    line.setAttribute("y1", lasty)
    line.setAttribute("x2", e.offsetX)
    line.setAttribute("y2", e.offsetY)
    line.setAttribute("stroke-width","5");
    line.setAttribute("stroke","black");
    pic.appendChild(line);
  }
  lastx=e.offsetX;
  lasty=e.offsetY;
});

var clearbtn = document.getElementById("clear");
clearbtn.addEventListener('click', clear);
