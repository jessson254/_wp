function uniqueSorted(arr) {
  return [...new Set(arr)].sort((a, b) => a - b);
}
const arr = [5, 3, 8, 3, 1, 5, 2];
console.log(uniqueSorted(arr)); 
// [1, 2, 3, 5, 8]
