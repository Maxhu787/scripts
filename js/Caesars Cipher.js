function rot13(str) {//65 90
    let arr = [];
    let answer = [];
    for (let i = 0; i < str.length; i++) {
        arr.push(str.charCodeAt(i));
    }
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == 32) {
            arr[i] = 32;
        } else if (arr[i] - 13 < 65) {
            arr[i] += 13;
        } else {
            arr[i] -= 13;
        }

    }
    for (let i = 0; i < arr.length; i++) {
        answer.push(String.fromCharCode(arr[i]));
    }
    return answer.join('');
}
console.log(rot13("SERR PBQR PNZC"));

