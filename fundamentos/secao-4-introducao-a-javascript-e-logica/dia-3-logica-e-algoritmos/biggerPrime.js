let firstNumber = 2;
let lastNumber = 50;
let lastPrime = 2;

for (let number = firstNumber; number <= lastNumber; number += 1) {
    isPrime = true; // assume que o número a ser verificado é primo
    for (index = 2; index < number; index += 1) {
        if (number % index == 0) {
            isPrime = false; //deu resto zero uma vez, já sei que não é primo
        }
    }
    if (isPrime == true) {
        lastPrime = number; //não teve resto zero, coloca na variável
    }
}

console.log('O maior número primo é ' + lastPrime);
