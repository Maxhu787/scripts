function smallestCommons(arr) {
  function answer(m, min, max) {
    for(var i = min; i < max; i++) {
      if(m % i != 0) {
        return false;
      }
    }
    return true;
  }
  let max = Math.max(arr[0], arr[1]);
  let min = Math.min(arr[0], arr[1]);
  let multiple = max;
  while(!answer(multiple, min, max)) {  
      multiple += max;
  }
  return multiple;
}
console.log(smallestCommons([1,5]));