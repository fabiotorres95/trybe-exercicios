let a = 2112;
let b = 505;
let c = 5555;

if (a > b && a > c) {
    console.log('O primeiro número é o maior.');
} else if (b > a && b > c) {
    console.log('O segundo número é o maior.');
} else if (c > a && c > b) {
    console.log('O terceiro número é o maior.');
} else {
    console.log('2 ou mais valores iguais são os maiores.');
}