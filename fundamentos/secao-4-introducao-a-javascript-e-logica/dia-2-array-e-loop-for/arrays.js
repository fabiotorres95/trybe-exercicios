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
// console.log(sum / numbers.length);

// Ponto 4
// let sum = 0;
// let average = 0;
// for (let number of numbers) {
//     sum  += number;
// }
// average = sum / numbers.length;
// if (average > 20) {
//     console.log('valor maior que 20');
// } else {
//     console.log('valor menor ou igual a 20');
// }

// Ponto 5
// let bigger = numbers[0];
// for (let index = 1; index < numbers.length; index += 1) {
//     if (bigger < numbers[index]) {
//         bigger = numbers[index];
//     }
// }
// console.log(bigger);

// Ponto 6
// let odd = 0;
// for (let index = 0; index < numbers.length; index += 1) {
//     if (numbers[index] % 2 == 1) {
//         odd += 1;
//     } 
// }
// if (odd == 0) {
//     console.log('nenhum valor ímpar encontrado');
// } else {
//     console.log(odd);
// }

// Ponto 7
// let smaller = numbers[0];
// for (let index = 1; index < numbers.length; index += 1) {
//     if (smaller > numbers[index]) {
//         smaller = numbers[index];
//     }
// }
// console.log(smaller);

//Pontos 8 e 9
// let newArray = [];
// for (let index = 1; index <= 25; index += 1) {
//     newArray.push(index);
// }
// console.log(newArray);

// for (let index = 0; index < newArray.length; index += 1) {
//     console.log(newArray[index] / 2);
// }