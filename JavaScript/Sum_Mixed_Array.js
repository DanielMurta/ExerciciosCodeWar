function sumMix(x) {
    let sum = 0
    for (let c = 0; c < x.length; c++) {
        sum += parseInt(x[c])
    }

    return sum
}


// test
console.log(sumMix([9, 3, '7', '3']))


// Another Solution
//let result = 0;
//  for (let n of x) {
//    result += parseInt(n);
//  }
//  return result;