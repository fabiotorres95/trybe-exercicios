const testingScope = (escopo) => {
  if (escopo === true) {
    let ifScope = 'Não devo ser utilizada fora do meu escopo (if)';
    ifScope = `${ifScope} ótimo, fui utilizada no escopo !`;
    console.log(ifScope);
  } else {
    const elseScope = 'Não devo ser utilizada fora do meu escopo (else)';
    console.log(elseScope);
  }
  console.log(`${ifScope} o que estou fazendo aqui ? :O`); // Se necessário esta linha pode ser removida.
}

// testingScope(true);

const crescent = (array) => array.sort();

// console.log(crescent([9,7,5,3,2,4,6,8]))

const oddsAndEvens = [13, 3, 4, 10, 7, 2];

const sortOddsAndEvens = (array) => {
  let sortedArray = [];
  while (sortedArray.length < array.length) {
    let smallestNumber = array[0];
    let smallestIndex = 0;
    for (let index = 1; index < array.length; index += 1) {
      if (array[index] < smallestNumber) {
        smallestNumber = array[index];
        smallestIndex = index;
      }
    }

    sortedArray.push(smallestNumber);
  }
};

console.log(`Os números ${sortOddsAndEvens(oddsAndEvens)} se encontram ordenados de forma crescente!`);