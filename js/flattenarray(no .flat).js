function steamrollArray(arr) {
    let answer = [];
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            answer.push(...steamrollArray(arr[i]))
        } else {
            answer.push(arr[i])
        }
    }
    return answer;
}

console.log(steamrollArray([1, [2], [3, [[4]]]]));