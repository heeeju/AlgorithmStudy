// 입력
    //reuslt idx에 문자 하나 추가.
    //idx++

// 인덱스 이동
    // <
        // 0이라면 인덱스 유지 & break;
        // 아니라면 인덱스 --
    // >
        // 최대(result길이)라면 인덱스 유지 & break;
        // 아니라면 인덱스 ++

// 지우기
    //반복
        //인덱스가 0이라면 -> Nothing
        //아니라면
            //글자 지우기
            //인덱스 -- (0이면 유지)

#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <list>
using namespace std;

//방법1. substring -> 시간초과
void Ans1(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int size;
    cin >> size;
    while(size--){
        string str;
        string result;
        cin >> str;
        int idx=0;
        for(int j=0; j<str.length(); j++){
            int len = result.length();
            switch(str[j]){
                case '<':
                    idx=max(--idx, 0);
                    break;
                case '>':
                    idx=min(++idx, len);
                    break;
                case '-':
                    if(idx==0);
                    else{
                        result.erase(idx-1,1);
                        idx=max(--idx, 0);
                    }
                    break;
                default:
                    string add;
                    add+=str[j];
                    result.insert(idx, add);
                    idx++;
                    break;
            }
        }
        //결과 출력
        cout << result ;
    }
}

//방법 2. List
void Ans2(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int size;
    cin >> size;
    while(size--){
        string str;
        cin >> str;
        list<char> result;
        list<char>::iterator iter = result.begin();
        for(int j=0; j<str.length(); j++){
            switch(str[j]){
                case '<':
                    if(iter!=result.begin()) iter--;
                    break;
                case '>':
                    if(iter!=result.end()) iter++;
                    break;
                case '-':
                    if(iter!=result.begin()){
                        result.erase((--iter)++);
                    }
                    break;
                default:
                    result.insert(iter, str[j]);
                    break;
            }
        }
        for(iter=result.begin(); iter!=result.end(); ++iter)
            cout << *iter;
        cout << endl;
    }
}

//방법3 Stack
//커서 앞 stack과 커서 뒤 stack을 만들어서 적절히 push & pop
void Ans3(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int size;
    cin >> size;
    while(size--){
        string str;
        cin >> str;
        stack<char> front;
        stack<char> back;
        for(int j=0; j<str.length(); j++){
            switch(str[j]){
                case '<':
                    if(!front.empty()){
                        back.push(front.top());
                        front.pop();
                    }
                    break;
                case '>':
                    if(!back.empty()){
                        front.push(back.top());
                        back.pop();
                    }
                    break;
                case '-':
                    if(!front.empty())
                        front.pop();
                    break;
                default:
                    front.push(str[j]);
                    break;
            }
        }
        while(!front.empty()){
            back.push(front.top());
            front.pop();
        }
        while(!back.empty()){
            cout << back.top();
            back.pop();
        }
        cout << endl;
    }
}

int main() {
    int no = 3;
    switch (no){
        case 1:
            Ans1();
            break;
        case 2:
            Ans2();
        case 3:
            Ans3();
    }
}