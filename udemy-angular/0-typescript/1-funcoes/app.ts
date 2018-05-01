let isEnoughToBeatMF = function (parsecs: number) : boolean {
  return parsecs < 12
}
let distance:number = 10
console.log(`Is ${distance} parsecs enough to beat Millennium Falcon? ${isEnoughToBeatMF(distance)?'Yes':'NO'}`)

let call = (name: string) => console.log(`Do you copy, ${name}?`)
call('R2')

function inc (speed: number, inc: number = 1) : number {
  return speed + inc
}
let p1:number = 34
let p2:number = 2
console.log(`inc (${p1},${p2}) = ${inc(p1,p2)}`)
console.log(`inc (${p1}) = ${inc(p1)}`)
