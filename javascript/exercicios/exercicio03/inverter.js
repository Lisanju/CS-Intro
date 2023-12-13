let v1 = [0,1,2,3];

function reverterModificar(v1){
    var conv = [];
    for(var i = 0; i < v1.length; i++){
        conv.unshift(v1[i]);
    }
    
    function modificarOriginal(v1){
        for(var i = 0; i < conv.length; i++){
            v1.push(conv[i]);
        }
        return v1;
    }
    modificarOriginal(v1);
    v1.splice(0,4);
    console.log(conv);
    return v1;
}
reverterModificar(v1);
console.log(v1);

let v2 = ["a","b","c","d"];

function reverterSemModificar(v2){
    var conv = [];
    for (var i = 0; i < v2.length; i++){
        conv.unshift(v2[i]);
    }
    
    v2.splice(4,4);
    console.log(conv);
    return v2;
}

reverterSemModificar(v2);
console.log(v2);
