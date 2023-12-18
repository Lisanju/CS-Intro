const gatos = Array("nana","tom","salem");

function reverterModificar(array){
    for (let i = 0; i < array.length; i++){
        array.unshift(array[i]);
        array.splice(i + 1, 1);
    }
    return array;
}

console.log(reverterModificar(gatos)); // salem, tom, nana

function reverterSemModificar(array){
    const arrayNovo = [];
    for (let i = 0; i < array.length; i++){
        arrayNovo.unshift(array[i]);
    }
    return arrayNovo;
}

console.log(reverterSemModificar(gatos));
