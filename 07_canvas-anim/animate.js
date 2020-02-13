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
    animate();
  }
}
  //console.log(mode);
var stop=document.getElementById("stop");
var ani=document.getElementById("animate");
stop.addEventListener('click', cancel);
ani.addEventListener('click', draw);
