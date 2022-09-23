let word = 'tryber';
let array = [];
newWord = '';

while (array.length < word.length) {
    array.unshift(word[array.length]);
}

for (let index = 0; index < array.length; index += 1) {
    newWord = newWord + array[index];
}
console.log(newWord);