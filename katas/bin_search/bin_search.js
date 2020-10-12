const p = console.log;
function array(size,limit){
    let arr = []
    for (i =0; i<size;i++){
        arr[i] = randomPositiveInt(limit);
    }
    return arr =  arr.sort((a,b)=>{return a-b}); 
}

function randomPositiveInt(maximum, minimum){
    const max = maximum ? maximum : 10;
    const min = minimum ? minimum : 1;
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const list = array(20,200);
const target = randomPositiveInt(10);
p(list);
p(target);