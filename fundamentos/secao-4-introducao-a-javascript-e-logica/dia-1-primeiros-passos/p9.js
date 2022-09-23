let angle1 = 30;
let angle2 = 60;
let angle3 = 90;

if (angle1 < 0 || angle2 < 0 || angle3 < 0) {
    console.log('ERRO! valores inválidos.');
} else if (angle1 + angle2 + angle3 == 180) {
    console.log('Os ângulos escolhidos formam um triângulo.');
} else {
    console.log('Os ângulos escolhidos não podem formar um triângulo.');
}