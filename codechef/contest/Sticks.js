function answer(sticks){
    let answer = new Set(sticks)
    return !answer.has(0) ? answer.size : answer.size - 1
}

const result = sticks => {
    let answer = new Set(sticks)
    return !answer.has(0) ? answer.size : answer.size - 1
}

console.log(answer([5,3,5]))
console.log(result([0,1,1,3,3]))