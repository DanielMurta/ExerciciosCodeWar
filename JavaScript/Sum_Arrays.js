function sum (numbers) {
    let sum = 0
    for (let c = 0; c < numbers.length; c++) {
        sum += numbers[c]
    }

    return sum
}

// test
sum([1, 5.2, 4, 0, -1])

// Outra Solução - Another Solution
// return numbers.reduce((a, b) => a + b, 0);