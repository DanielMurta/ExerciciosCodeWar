var summation = function (num) {
    let sum = 0
    for (let c = 0; c <= num; c++){
        sum += c
    }

    return sum
}


// test
console.log(summation(1))
console.log(summation(2))
console.log(summation(8))


// Another Solution
// return num * (num + 1) / 2