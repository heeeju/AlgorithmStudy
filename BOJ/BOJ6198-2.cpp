#include <bits/stdc++.h>
using namespace std;

//point -> 내가 볼 수 있는 빌딩의 개수를 구하지 말고 나를 볼 수 있는 빌딩의 개수를 구하자.
int n; //최대 80000개 -> int로 가능 
int b[800001]; //빌딩 높이 최대 1,000,000,000 - int로 가능
long long sum; //최대 79999+...+1 = 80000 * 40000 = 3,200,000,000 (3억) -> Int로 안됨

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    cin >> n;
    for(int i=0; i<n; i++)
        cin >> b[i];
    
    stack<int> s;
    for(int i=0; i<n; i++){
        while(!s.empty() && s.top()<= b[i])
            s.pop();
        sum+=s.size();
        s.push(b[i]);
    }
    cout << sum;
    return 0;
}
