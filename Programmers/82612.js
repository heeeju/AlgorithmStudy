function solution(price, money, count) {
    var answer = (count+1)*count / 2 * price -  money;
    if (answer <= 0) answer = 0;

    return answer;
}
