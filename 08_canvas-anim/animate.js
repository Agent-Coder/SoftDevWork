//Devin Lin and Amanda Zheng (Team Fridge Ninjas)
//SoftDev1 pd1
//K#07 -- Canvas-anim
//2020-02-12

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var r=10;
var id;
var expand=true;
var animating=false;
var img=new Image();
var x;
var y;
var dx=5;
var dy=-5;
img.src = 'dvd.png'

ctx.beginPath();
ctx.arc(300, 300, r, 0, 2 * Math.PI);
ctx.stroke();
ctx.fill();
ctx.closePath();

var cancel = function(){
  if (id!=null){
    window.cancelAnimationFrame(id)
    animating=false;
  }//console.log(mode);
}



var animate = function(){
  animating=true;
  if(expand){
    r+=5
    ctx.beginPath();
    ctx.arc(300, 300, r, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    ctx.closePath();
  }else{
    r-=5
    ctx.clearRect(0,0,c.width,c.height);
    ctx.beginPath();
    ctx.arc(300, 300, r, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    ctx.closePath();
    }
  if (r==300 || r==10){
      expand=!expand;
  }
  id=window.requestAnimationFrame(animate);
}

var draw = function(){
  if(!animating){
    cancel();
    ctx.clearRect(0,0,c.width,c.height);
    animate();
  }
}

var movie = function(){
  ctx.clearRect(0,0,c.width,c.height);
  cancel();
  x=Math.floor(Math.random()*400)+100;
  y=Math.floor(Math.random()*400)+100;
  dvd();
}

var dvd = function(){
  animating=false;
  ctx.clearRect(0,0,c.width,c.height);
  ctx.beginPath();
  if(y+dy<0){
    dy=Math.abs(dy)
  }
  if(y+dy>525){
    dy=-1*Math.abs(dy)
  }
  if(x+dx<0){
    dx=Math.abs(dx)
  }
  if(x+dx>485){
    dx=-1*Math.abs(dx)
  }
  x+=dx;
  y+=dy;
  ctx.drawImage(img,x,y,125,75);
  ctx.closePath();
  id=requestAnimationFrame(dvd);
}
  //console.log(mode);
var stop=document.getElementById("stop");
var ani=document.getElementById("animate");
var bounce=document.getElementById("movie");
stop.addEventListener('click', cancel);
ani.addEventListener('click', draw);
bounce.addEventListener('click',movie)
