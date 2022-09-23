let percentage = 0; // valor do usuário
let grade;

if (percentage > 100 || percentage < 0) {
    grade = 'ERROR: not a valid percentage';
} else if (percentage >= 90) {
    grade = 'A';
} else if (percentage >= 80) {
    grade = 'B';
} else if (percentage >= 70) {
    grade = 'C';
} else if (percentage >= 60) {
    grade = 'D';
} else if (percentage >= 50) {
    grade = 'E';
} else {
    grade = 'F';
}

console.log(grade);