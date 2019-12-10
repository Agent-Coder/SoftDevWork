var fact = function(n){
    if(n <= 1){
      return 1;
    }
    return n*fact(n-1);
};

// console.log(fact(12));

var fib = function(n){
    if(n <= 2){
      return 1;
    }
    return fib(n-2)+fib(n-1);
};

// console.log(fib(8));

var gcd = function(a,b){
    if(a % b == 0){
      return b;
    }
    return gcd(b, a % b);
};

// console.log(gcd(16,8));

var students = ["a","b","c","d"]
var randomStudent = function(){
    var i = Math.round(Math.random()*students.length);
    return students[i];
};

console.log(randomStudent());
