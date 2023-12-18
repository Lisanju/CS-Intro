function retornaPalindromos(array){
    const vetorPalindromos = [];
    for (let i = 0; i < array.length; i++){
        let stringCheck = "";
        for (let e = 0; e < array[i].length; e++){
            stringCheck = array[i][e] + stringCheck;
        }
        if (array[i] === stringCheck){
            vetorPalindromos.push(array[i]);
        }
    }
    return vetorPalindromos;
}

const vetor = Array("nana","gato","ovo","reviver","pedro","arara");
console.log(retornaPalindromos(vetor));
