function pairwise(arr, arg) {
    let x = [];
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (j == i) {
                continue;
            } else {
                if ((arr[i] + arr[j]) == arg) {
                    let y = []
                    y.push(i);
                    y.push(j);
                    y.sort();
                    x.push(y);
                }
            }
        }
    }
    return x
    // return x.reduce((x, y) => x + y, 0);
}

// console.log(pairwise([1,4,2,3,0,5], 7));
console.log(pairwise([7, 9, 11, 13, 15], 20));