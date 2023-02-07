function paperwork(n, m) {
    if (n < 0 || m < 0) {
        return 0
    }

    return n * m
}

// test
console.log(paperwork(5, 5))
console.log(paperwork(5, -5))
console.log(paperwork(-5, 5))
console.log(paperwork(-5, -5))

// Another Solution
// return n > 0 && m > 0 ? n * m : 0