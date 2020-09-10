function solution(matrix) {
    let count = 0
    for (let i = matrix.length-1; i > 0; i--) {
        if (matrix[i][i] != matrix[i][i-1]+1){
            count++
            next = i + 1
            for (let j = 0; j < next; j++){
                for (let k = j; k < next; k++){
                    matrix[j][k], matrix[k][j] = matrix[k][j], matrix[j][k]
                }
            }
        }
        else{
            continue
        }
    }
    return count
}

let matrix = [[1,2,9,13], [5,6,10,14], [3,7,11,15], [4,8,12,16]]
console.log(solution(matrix));