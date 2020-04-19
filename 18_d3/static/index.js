count=0
//var data =  [{"country":"Canada","cases":canada[0]},
//{"country":"China","cases":china[0]},{"country":"France","cases":france[0]},
//{"country":"Gernmany","cases":germany[0]},
//{"country":"Iran","cases":iran[0]},{"country":"Italy","cases":italy[0]},
//{"country":"Korea","cases":korea[0]},{"country":"Spain","cases":spain[0]}
//,{"country":"United Kingdom","cases":uk[0]},{"country":"United States","cases":us[0]}]
   //Select your chart.
var data=[canada[0],china[0],france[0],germany[0],iran[0],italy[0],korea[0],spain[0],uk[0],us[0]]
var chart = d3.select(".chart");
 //Prepare for data join.
var bar = chart.selectAll("div");
  // (this defines selection to which you will join data)
   //Join your data.
var barUpdate = bar.data(data);
   //Instantiate new elements by appending to the “enter selection.”
var barEnter = barUpdate.enter().append("div");
console.log(5)
 //Set width of each bar proportional to its data value.
barEnter.style("width", function(d) {return d * 10 + "px"; });
   //Label each bar.
barEnter.text(function(d) { return d; });
