function highAndLow(numbers) {
    let lista = []
    let array = numbers.split(' ')
    for (let numero in array){
        lista.push(parseInt(array[numero]))
    }

    return `${Math.max(...lista)} ${Math.min(...lista)}`
}

// test
console.log(highAndLow("1 2 3 4 5"))
//highAndLow("1 2 -3 4 5")
//highAndLow("1 9 3 4 -5")


// Another Solution
// numbers = numbers.split(' ');
// return `${Math.max(...numbers)} ${Math.min(...numbers)}