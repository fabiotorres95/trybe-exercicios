let numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]; //array para todos os exercícios

// Ponto 1
// for (let number of numbers) {
//     console.log(number);
// }

// Ponto 2
// let sum = 0;
// for (let number of numbers) {
//     sum += number;
// }
// console.log(sum);

// Ponto 3
// let sum = 0;
// for (let number of numbers) {
//     sum  += number;
// } 
// console.log(sum / numbers.length)

// Ponto 4
let sum = 0;
let average = 0;
for (let number of numbers) {
    sum  += number;
}
average = sum / numbers.length;
if (average > 20) {
    console.log('valor maior que 20');
} else {
    console.log('valor menor ou igual a 20');
}