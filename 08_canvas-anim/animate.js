//Devin Lin and Amanda Zheng (Team )
//SoftDev1 pd1
//K#07 -- Canvas-anim
//2020-02-12

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var r=10;
var id;
var expand=true;
var animating=false;
var move=false;
var img=new Image();
var x;
var y;
var dx=10;
var dy=10;
img.src = 'dvd.jpg'

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
    ctx.clearRect(0,0,ctx.width,ctx.height);
    animate();
  }
}

var movie = function(){
  if(!move){
    cancel();
    console.log("hi");
    ctx.clearRect(0,0,ctx.width,ctx.height);
    x=Math.floor(Math.random()*590);
    y=Math.floor(Math.random()*590);
    dvd();
  }
}

var dvd = function(){
  ctx.drawImage(img,x,y);
  ctx.beginPath();
  if( x<10|| y<10 || x>590||y>590 ){
    dx=-dx;
    dy=-dy;
  }
  x+=dx;
  y+=dy;
  ctx.drawImage(img,x,y);
}
  //console.log(mode);
var stop=document.getElementById("stop");
var ani=document.getElementById("animate");
var bounce=document.getElementById("movie");
stop.addEventListener('click', cancel);
ani.addEventListener('click', draw);
bounce.addEventListener('click',movie)
