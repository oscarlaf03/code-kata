
// helper function to see if two different strings have the same length and chars 
function areAnagrams(word,target){
    if (word === target){ // cannot be anagram of itself for purpose of filtering
        return false;
    }else if (word.length != target.length ){
        return false;
    } else {
        let letters = word.split('');
        let counter = letters.length;
        letters.forEach( l => {
            if (!target.includes(l)){
                counter -= 1
            }
        });
        return counter == target.length;
    }
}

function funWithAnagrams(text) {
    const toFilter = [];
    text.forEach( (word) =>{
        text.forEach(w => {
            if(areAnagrams(word,w)&& !toFilter.includes(word)){
                toFilter.push(w)
            }
        })
    })
    filteredArray = text.filter(e => !toFilter.includes(e))
    return [... new Set( filteredArray)]; // removes duplicate from the array
}


const test = ["code",'code',"aaagmnrs","anagrams","doce"];

console.log(funWithAnagrams(test));