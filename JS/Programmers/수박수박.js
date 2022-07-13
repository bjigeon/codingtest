function solution(n) {
    var answer = [];
    for (let i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            answer.push('박')
        }
        else {
            answer.push('수')
        }
    }

    return answer.join('')
}