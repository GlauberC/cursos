// Para ir criando o app.js
// basta no console deixar em background o comando tsc -w

// Para executar o arquivo app.js basta no terminal executar node app.js
let message: string = "Help me, Obi-Wan Kenobi. You're my only hope!"
console.log(message)

let episode: number =4
console.log("This is episode " + episode)
episode++
console.log("Next episode is " + episode)

//let favoriteDroid // Voce pode colocar any ou esconder o tipo da variavel
                    // Mas o ideal eh desclarar o tipo

let favoriteDroid: string
favoriteDroid = "BB-8"
//favoriteDroid = 10  //Ao declarar o tipo essa linha ocasionará um erro
console.log("My favorite droid is " + favoriteDroid)