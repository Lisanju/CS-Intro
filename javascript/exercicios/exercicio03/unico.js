function valoresUnicos(array){
    const arrayVU = [];
    for (let i = 0; i < array.length; i++){
        if (arrayVU.includes(array[i]) === false){
            arrayVU.push(array[i]);
        }
    }
    return arrayVU;
}

const gatos = Array("tom","tom","nana","salem","nana","brisa","nana");

console.log(valoresUnicos(gatos));
