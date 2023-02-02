function oddOrEven(array) {
    var soma = 0
    for (var i = 0; i < array.length; i++) {
        soma += array[i]
    } if (soma % 2 == 0) {
        return 'even'
    } else {
        return 'odd'
    }
}

// Test
oddOrEven([0, 1, 5])


// Outra Solução - Another Solution
// return arr.reduce((a,b)=>a+b,0) % 2 ? 'odd' : 'even';
