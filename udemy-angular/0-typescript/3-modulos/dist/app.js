"use strict";
exports.__esModule = true;
var starfighters_1 = require("./starfighters");
var goodForTheJob = function (ship) { return ship.cargoContainers > 2; };
var falcon = new starfighters_1.MillenniumFalcon();
falcon.jumpIntoHyperSpace();
console.log("Is falcon good for the job? " + (goodForTheJob(falcon) ? 'YES' : 'NO'));
