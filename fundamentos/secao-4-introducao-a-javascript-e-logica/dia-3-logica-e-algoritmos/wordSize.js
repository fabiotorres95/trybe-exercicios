let array = ['java', 'javascript', 'python', 'html', 'css'];
bigger = 0;
smaller = 0;

for (let index = 1; index < array.length; index += 1) {
    if (array[bigger].length < array[index].length) {
        bigger = index;
    }
    if (array[smaller].length > array[index].length) {
        smaller = index;
    }
}

console.log('A maior palavra é ' + array[bigger]);
console.log('A menor palavra é ' + array[smaller]);