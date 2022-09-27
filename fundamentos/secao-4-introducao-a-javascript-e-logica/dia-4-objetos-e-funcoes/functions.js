function VerificaPalindrome(word) {
    let splitWord = word.split('');
    splitWord.reverse();
    let drow = splitWord.join('');
    if (word === drow) {
        return true;
    } else {
        return false;
    }   
}

console.log(VerificaPalindrome('arara'));