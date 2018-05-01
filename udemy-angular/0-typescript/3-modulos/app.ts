import {Spacecraft, Containership} from './base-ships'
import {MillenniumFalcon} from './starfighters'


let goodForTheJob = (ship: Containership) => ship.cargoContainers > 2

let falcon = new MillenniumFalcon()

falcon.jumpIntoHyperSpace()

console.log(`Is falcon good for the job? ${goodForTheJob(falcon)?'YES': 'NO'}`)
