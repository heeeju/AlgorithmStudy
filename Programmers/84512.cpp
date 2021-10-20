#include <string>

using namespace std;

int solution(string word) {
    int key[5]={781,156,31,6,1};
    int answer = 0;
    for(int i=0; i<word.size(); i++){
        if(word[i]=='A'){
            answer += 1;
        }else if(word[i]=='E'){
            answer += 1 + key[i] * 1;
        }else if(word[i]=='I'){
            answer += 1 + key[i] * 2;
        }else if(word[i]=='O'){
            answer += 1 + key[i] * 3;
        }else if(word[i]=='U'){
            answer += 1 + key[i] * 4;
        }
    }
    return answer;
}
