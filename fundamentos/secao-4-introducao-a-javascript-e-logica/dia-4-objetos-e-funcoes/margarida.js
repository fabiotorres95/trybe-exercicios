let info = {
    personagem: 'Margarida',
    origem: 'Pato Donald',
    nota: 'Namorada do personagem principal nos quadrinhos do Pato Donald',
    recorrente: 'Sim',
  };

//   console.log('Bem vinda, ' + info.personagem);
//   console.log(info);
// for (let key in  info) {
//     console.log(key);
// };
// for (let key in info) {
//     console.log(info[key]);
// };
let newInfo = {
    personagem: 'Tio Patinhas',
    origem: "Christmas on Bear Mountain, Dell's Four Color Comics #178",
    nota: 'O último MacPatinhas',
    recorrente: 'Sim',
}

for (let key in info) {
    if (key === 'recorrente') {
        if (info[key] === newInfo[key]) {
            console.log('Ambos recorrentes');
            break;
        } else if (info[key] === 'Sim') {
            console.log('Só o primeiro é recorrente');
            break;
        } else {
            console.log('Só o segundo é recorrente');
            break;
        }
    }
    console.log(info[key] + ' e ' + newInfo[key]);
}