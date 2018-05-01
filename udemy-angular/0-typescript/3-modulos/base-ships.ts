class Spacecraft {
  constructor(public propulsor: string){}

  jumpIntoHyperSpace(){
    console.log(`Entering hyperspace with ${this.propulsor}`)
  }//jumpIntoHyperSpace
}//class


interface Containership{
  cargoContainers: number
} //interface

export{
  Spacecraft,
  Containership
}
