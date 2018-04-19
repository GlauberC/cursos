var parameters = {
  target: '.graph',
  data: [
{ 
    fn: 'sin(x)', //First Function
    color: 'green'
},    
],
  grid: true,
  yAxis: {domain: [-1, 1]},
  xAxis: {domain: [0, 2*Math.PI]}
};

function plot(){
    var color = document.querySelector("#color").value;
    var yMin = document.querySelector("#yMin").value;
    var yMax = document.querySelector("#yMax").value;
    var xMin = document.querySelector("#xMin").value;
    var xMax = document.querySelector("#xMax").value;
    var func = document.querySelector("#func").value;
    parameters.data[0].color=color;
    parameters.xAxis.domain = [xMin, xMax];
    parameters.yAxis.domain = [yMin, yMax];
    parameters.data[0].fn = func;

    functionPlot(parameters);
    
}


