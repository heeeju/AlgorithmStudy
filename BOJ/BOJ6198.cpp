#include <bits/stdc++.h>
using namespace std;

//시간 초과
int n; //최대 80000개 -> int로 가능 
int b[800001]; //빌딩 높이 최대 1,000,000,000 - int로 가능
long long sum; //최대 79999+...+1 = 80000 * 40000 = 3,200,000,000 (3억) -> Int로 안됨

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    cin >> n;
    for(int i=0; i<n; i++)
        cin >> b[i];
    
    for(int i=0; i<n; i++){
        stack<int> s;
        for(int j=i+1; j<n; j++){
            if(b[i] > b[j]) 
                s.push(b[j]);
            else break;
        }
        //cout << s.size() << '\n';
        sum += s.size();
    }
    cout << sum;
    return 0;
}
