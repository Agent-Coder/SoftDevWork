//Jackie Lin and Amanda Zheng (Team DJAJ)
//SoftDev1 pd1
//K#03 -- Canvas
//2020-02-05

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var colors=["black","green","yellow","purple","red","blue","brown","orange","pink","grey"]
var colorIndex=0
ctx.fillStyle = colors[colorIndex]
ctx.strokeStyle = colors[colorIndex]
var mode = 0; //0 for dot, 1 for box

var clear = function(){
  ctx.clearRect(0, 0, c.width, c.height);
  //console.log("clear");
}

var toggle = function(){
  if (mode == 0){
    mode = 1;
    document.getElementById("mode").innerHTML = "box";
  }
  else {
    mode = 0;
    document.getElementById("mode").innerHTML = "dot";
  }
  //console.log(mode);
}

var colorize = function(){
  //console.log("hi")
  colorIndex=(colorIndex+1)%10;
  ctx.fillStyle=colors[colorIndex];
  ctx.strokeStyle = colors[colorIndex];
  document.getElementById("CurrentColor").innerHTML = colors[colorIndex];
}

c.addEventListener('mousedown', e => {
  var x = e.pageX - c.offsetLeft;
  var y = e.pageY - c.offsetTop;
  if (mode == 1){
    ctx.fillRect(x, y, 20, 20);
  }
  else {
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
  }
});

var clearbtn = document.getElementById("clear");
clearbtn.addEventListener('click', clear);

var togglebtn = document.getElementById("toggle");
togglebtn.addEventListener('click', toggle);

var colorizebtn = document.getElementById("color");
colorizebtn.addEventListener('click', colorize);
