function findNeedle(haystack) {
    let index = haystack.indexOf('needle')
    return `found the needle at position ${index}`
}

// test
findNeedle(['3', '123124234', undefined, 'needle', 'world', 'hay', 2, '3', true, false])

// Another Solution
// return "found the needle at position " + haystack.indexOf("needle")