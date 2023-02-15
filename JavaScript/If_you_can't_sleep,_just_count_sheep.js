var countSheep = function (num){
    let count = []
    if (num < 1){
        return ''
    } else {
        for (let c = 1;c < num + 1; c++){
            count.push(`${c} sheep...`)
        }
    }

    return string = count.join('')
    
}

// test
console.log(countSheep(5))

// Another Solution
//let str = "";
//  for(let i = 1; i <= num; i++) { str+= `${i} sheep...`; }
//  return str;
