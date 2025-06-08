function filterArray(arr, predicate) {
    const result = [];
    for (let i = 0; i < arr.length; i++) {if (predicate(arr[i])) {
        result.push(arr[i]);
      }
    }
    return result;
  }

  console.log(filterArray([1, 2, 3, 4, 5], n => n % 2 === 0)); 
