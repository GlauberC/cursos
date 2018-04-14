var parameters = {
  target: '#myFunction',
  data: [
{ 
    fn: 'sin(x)', //First Function
    color: 'green'
},    
{
    fn: 'cos(x)',
    color:'red'    
},
{
    fn:'tan(x)',
    color:'blue'
}
        ],
  grid: true,
  yAxis: {domain: [-1, 1]},
  xAxis: {domain: [0, 2*Math.PI]}
};

functionPlot(parameters);