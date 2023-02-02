// Square(n) Sum
function squareSum(numbers) {
    let sum = 0
    for (let c = 0; c < numbers.length; c++){
        sum += numbers[c] ** 2
    }

    return sum
}  

// test
console.log(squareSum([1, 2]))

// Another Solution
// return numbers.reduce((sum,num) => sum + (num * num), 0)