var isEnoughToBeatMF = function (parsecs) {
    return parsecs < 12;
};
var distance = 10;
console.log("Is " + distance + " parsecs enough to beat Millennium Falcon? " + (isEnoughToBeatMF(distance) ? 'Yes' : 'NO'));
var call = function (name) { return console.log("Do you copy, " + name + "?"); };
call('R2');
function inc(speed, inc) {
    if (inc === void 0) { inc = 1; }
    return speed + inc;
}
var p1 = 34;
var p2 = 2;
console.log("inc (" + p1 + "," + p2 + ") = " + inc(p1, p2));
console.log("inc (" + p1 + ") = " + inc(p1));
