"use strict";
exports.__esModule = true;
var Pokemon = /** @class */ (function () {
    function Pokemon(nome) {
        this.nome = nome;
    }
    Pokemon.prototype.falar = function () {
        console.log("" + this.nome);
    };
    return Pokemon;
}());
exports.Pokemon = Pokemon;
