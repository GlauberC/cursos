
function exemplo1(){ // test() - testa uma expressao regular
    var re = /JavaScript/;
    var string = "Nessa expressão há JavaScript?";
    var cmd = re.test(string);
    console.log("test() function: " + cmd);
}

function exemplo2(){ //modf i - ignora case sensitive 
    var re = /JavaScript/;
    var re2 = /JavaScript/i;

    var string = "Nessa expressão há javascript?";
    var cmd = re.test(string);
    var cmd2 = re2.test(string);
    console.log("Com case sensitive: "+ cmd);
    console.log("Sem case sensitive: "+ cmd2);
}

function exemplo3(){ //Exec - Retorna a primeira ocorrencia
    var re = /JavaScript/i;

    var string = "Nessa expressão há javascript?";
    var cmd = re.exec(string);
    console.log("com exec: "+ cmd);

}

function exemplo4(){ //Match e modf g
    var re = /java/ig;

    var string = "Eu vi um JaVaScript, Java, javali";
    var cmd = string.match(re);
    console.log("match com modf g: "+ cmd);
}

function exemplo5(){ //metachar . - encontra qualquer charactere
    var re = /./g;

    var string = "Test1234_!@#$";
    var cmd = string.match(re);
    console.log("metachar . :  "+ cmd);
}

function exemplo6(){ //metachar w - encontra qualquer charactere A-Z 0-9 _
    var re = /\w/g;

    var string = "Test1234_!@#$";
    var cmd = string.match(re);
    console.log("metachar w :  "+ cmd);
}

function exemplo7(){ //metachar s - Procura ocorrencia de espaços
    var re = /\s/g;

    var string1 = "SemEspaço:";
    var string2 = "Com Espaço: ";
    var cmd1 = re.test(string1);
    var cmd2 = re.test(string2);
    console.log(string1 + cmd1);
    console.log(string2 + cmd2);
}

function exemplo8(){ //metachar d - encontra digitos
    var re = /\d/g;

    var string = "Test1234_!@#$";
    var cmd = string.match(re);
    console.log("metachar d :  "+ cmd);
}

function exemplo9(){ //metachar ^ - Encontra char(s) que começa(am) com aquele(s) char(s)
    var re = /^1/;

    var string1 = "1test: ";
    var string2 = "test1: ";
    var cmd1 = re.test(string1);
    var cmd2 = re.test(string2);
    console.log(string1 + cmd1);
    console.log(string2 + cmd2);
}

function exemplo10(){ //metachar $ - Encontra char(s) que termina(am) com aquele(s) char(s)
    var re = /1$/;

    var string1 = "1test: ";
    var string2 = "test1";
    var cmd1 = re.test(string1);
    var cmd2 = re.test(string2);
    console.log(string1 + cmd1);
    console.log(string2 + ' ' + cmd2);
}

function exemplo11(){ //Quantificadores - * -> 0 ou mais / + -> uma ou mais / ? -> 0 ou 1 vez / {n} -> numero de vezes
    var re1 = /\d*/;
    var re2 = /\d+/;
    var re3 = /\d?/;
    var re4 = /\d{3}/;
    var re5 = /\d{2,3}/;

    var string1 = "test: ";
    var string2 = "test1: ";
    var string3 = "test11: ";
    var string4 = "test111: ";

    var cmd1 = re1.test(string1);
    var cmd2 = re2.test(string1);
    var cmd3 = re2.test(string2);
    var cmd4 = re3.test(string2);
    var cmd5 = re3.test(string3);
    var cmd6 = re4.test(string3);
    var cmd7 = re4.test(string4);
    var cmd8 = re5.test(string2);
    var cmd9 = re5.test(string3);
    var cmd10 = re5.test(string4);

    console.log(re1 + " " + string1 + cmd1);
    console.log(re2 + " " + string1 + cmd2);
    console.log(re2 + " " + string2 + cmd3);
    console.log(re3 + " " + string2 + cmd4);
    console.log(re3 + " " + string3 + cmd5);
    console.log(re4 + " " + string3 + cmd6);
    console.log(re4 + " " + string4 + cmd7);
    console.log(re5 + " " + string2 + cmd8);
    console.log(re5 + " " + string3 + cmd9);
    console.log(re5 + " " + string4 + cmd10);
}
function exemplo12(){ //[] chars opcionais 
    var re1 = /c[au]t/g;
    var re2 = /\d+[\.\d]*/g;

    var string1 = "cat cet cit cot cut" ;
    var string2 = "1 100 1.2 102.32 0.0" ;
    var cmd1 = string1.match(re1);
    var cmd2 = string2.match(re2);
    console.log(re1 + " " + cmd1);
    console.log(re2 + " " + cmd2);
}
function exemplo13(){ //replace
    var re = /\d/g;

    var string = "a1b2c3d4e5f1234";
    var cmd = string.replace(re,"n");
    console.log("string "+ string +  " to - : " + cmd);
}

function exemplo14(){ //$ para pegar trecho da expressao
    var re = /(\d)/g;

    var string = "a1b2c3d4e5f1234";
    var cmd = string.replace(re,"'$1");
    console.log("string "+ string +  " to - : " + cmd);
}