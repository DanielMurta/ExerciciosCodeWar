function sumArray(array){
    if (array == null) {
        return 0;
      } else if (array.length < 2) {
        return 0;
      } else {
        array = array.sort(function(a,b) {return a - b;});
        var total = 0;
        for (var i = 1; i < array.length - 1; i++) {
          total += array[i];
        }
        return total;
      }
    }

    



// test
console.log(sumArray([]))
console.log(sumArray([ 6 ]))
console.log(sumArray([ 6, 2 ]))
console.log(sumArray([ 6, 2, 1, 8, 10 ]))
console.log(sumArray([ 0, 1, 6, 10, 10 ]))