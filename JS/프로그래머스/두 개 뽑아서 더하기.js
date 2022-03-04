function solution(numbers) {
    
    let Nanswer = [];
    for (let i = 0; i < numbers.length; i++) {
        for (let j = 0; j < numbers.length; j++) {
            if(i == j){
                continue;
            }
            Nanswer.push(numbers[i] + numbers[j])
        }
    }
    const answer= Array.from(new Set(Nanswer))
    answer.sort()
    
    return answer;
}


console.log(solution(arr))
