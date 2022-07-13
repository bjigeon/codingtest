function solution(arr)
{
    var answer = [];

    let temp = -1
    for (let i = 0; i < arr.length; i++) {
        if (temp === arr[i]) continue
        else {
            temp = arr[i]
            answer.push(temp)
        }
    }
    
    return answer;
}