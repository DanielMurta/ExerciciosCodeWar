function getGrade (s1, s2, s3) {
    var avg = (s1 + s2 + s3) / 3
  if (avg >= 90)
  	return 'A'
  if (avg >= 80)
  	return 'B'
  if (avg >= 70)
  	return 'C'
  if (avg >= 60)
  	return 'D'
  return 'F'
}


// test
//console.log(getGrade(95,90,93))
console.log(getGrade(70,70,100))
//console.log(getGrade(70,70,70))
//console.log(getGrade(65,70,59))
//console.log(getGrade(44,55,52))
