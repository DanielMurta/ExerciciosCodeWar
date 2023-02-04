const areaOrPerimeter = function(l , w) {
    if (l != w) {
        return l * 2 + w * 2
    } else {
        return l * w
    }
  };


// Anoter solution
// return l == w ? l*w : 2*(l + w)