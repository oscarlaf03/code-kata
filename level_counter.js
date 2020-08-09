// https://www.hackerrank.com/challenges/counting-valleys/problem?
const s =  'UDDDUDUU';
const n = 8;

function countingValleys(n,s){
    let counter = 0;
    let valleys = 0;
    
    const stepsValue = s.split('').map( e =>  e === 'U' ? 1 : -1);
    stepsValue.array.forEach(step => {
        counter += step;
        if (counter === -1){
            valleys +=1;
        }
    });
    

}

countingValleys(n,s)