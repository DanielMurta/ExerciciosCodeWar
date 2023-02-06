function updateLight(current) {
    if (current == 'green') {
        return 'yellow'
    } else if (current == 'yellow') {
        return 'red'
    } else if (current == 'red') {
        return 'green'
    }
}

// test
console.log(updateLight('green'))
console.log(updateLight('yellow'))
console.log(updateLight('red'))

// Another solution
// return current === 'yellow' ? 'red' : current === 'green' ? 'yellow' : 'green'