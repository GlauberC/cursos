"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
exports.__esModule = true;
var pokegeral_1 = require("./pokegeral");
var Charizard = /** @class */ (function (_super) {
    __extends(Charizard, _super);
    function Charizard() {
        return _super.call(this, "Charizard") || this;
    }
    Charizard.prototype.falar = function () {
        console.log("raaaawr");
    };
    return Charizard;
}(pokegeral_1.Pokemon));
exports.Charizard = Charizard;
