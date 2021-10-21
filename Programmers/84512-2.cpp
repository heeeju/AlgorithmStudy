#include <string>

using namespace std;

int solution(string word) {
    int weights[5]={781,156,31,6,1};
    string key = "AEIOU";
    int answer = 0;
    for(int i=0; i<word.size(); i++){
        answer += 1 + (key.find(word[i])) * weights[i];
    }
    return answer;
}
