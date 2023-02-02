// Reduce but Grow

function grow(x) {
    let total = 1
    for (let c = 0; c < x.length; c++) {
        total *= x[c]
    }

    return total
}

// test
console.log(grow([1, 2, 3]))

// Another solution
// const grow=x=> x.reduce((a,b) => a*b);