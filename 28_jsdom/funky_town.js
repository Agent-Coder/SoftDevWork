//Amanda Zheng and Yvgeniy Gorbachev
//Softdev pd 1
//K27 -- Sequential Progression
//12-11-2019
var fact = function(n){
    if(n <= 1){
      return 1;
    }
    return n*fact(n-1);
};

var fibarray = [0,1,1];
var fib = function(n){
    if (fibarray[n]){
      return fibarray[n];
    }
    fibarray[n] = fib(n-1) + fib(n-2);
    return fibarray[n];
};

var gcd = function(a,b){
    if(a % b == 0){
      return b;
    }
    return gcd(b, a % b);
};

var selectRandom = function(array){
    return array[Math.floor(Math.random()*array.length)];
};
