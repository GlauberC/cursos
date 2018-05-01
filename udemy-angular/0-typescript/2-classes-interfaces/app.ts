class Spacecraft {
  constructor(public propulsor: string){}

  jumpIntoHyperSpace(){
    console.log(`Entering hyperspace with ${this.propulsor}`)
  }//jumpIntoHyperSpace
}//class
class MillenniumFalcon extends Spacecraft implements Containership{
  cargoContainers: number
  constructor(){
    super('hyperdrive')
    this.cargoContainers = 2
  }//class
  jumpIntoHyperSpace(){
    if(Math.random() >= 0.5){
      super.jumpIntoHyperSpace()
    }else {
      console.log('Failed to jump into hyperspace')
    }//else
  }//jumpIntoHyperSpace
}//class

interface Containership{
  cargoContainers: number
} //interface

let goodForTheJob = (ship: Containership) => ship.cargoContainers > 2

/*
let ship = new Spacecraft('hyperdrive')
ship.jumpIntoHyperSpace()
*/
let falcon = new MillenniumFalcon()
falcon.jumpIntoHyperSpace()
console.log(`Is falcon good for the job? ${goodForTheJob(falcon)?'YES': 'NO'}`)
