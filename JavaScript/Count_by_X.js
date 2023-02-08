function countBy(x, n){
    let z = []
    for (let c = 0; c < n; c++){
        z.push((c + 1) * x)
    }

    return z
}


// test
console.log(countBy(1, 10))
console.log(countBy(2, 5))


