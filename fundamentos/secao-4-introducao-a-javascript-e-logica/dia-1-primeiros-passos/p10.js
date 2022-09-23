let piece = 'Knight'; // input do usuário
piece = piece.toLowerCase();

switch(piece) {
    case 'pawn': 
        console.log('forward one space');
        break;
    case 'rook':
        console.log('cross');
        break;
    case 'knight':
        console.log('L shape');
        break;
    case 'bishop':
        console.log('diagonals');
        break;
    case 'queen':
        console.log('cross and diagonals');
        break;
    case 'king':
        console.log('cross and diagonals, one space');
        break;
    default:
        console.log('ERROR: not a chess piece');
}   