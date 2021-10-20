#include <bits/stdc++.h>
using namespace std;

//하나씩 비교 + 0인경우만 dp로 확인
//시간 초과
stack<int> s[2];
int dp[500001];

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int n;
    cin >> n;
    for(int i=1; i<=n; i++){
        int h;
        cin >> h;
        s[(i-1)%2] = s[i%2];
        s[(i-1)%2].push(h);

        int idx = i-1;
        while(!s[i%2].empty()){
            if(s[i%2].top()>h) {
                cout << idx << ' ';
                dp[i]= idx;
                break;
            }
            else if(dp[idx]==0){
                cout << 0 << ' ';
                dp[i] = 0;
                break;
            }
            s[i%2].pop();
            idx--;
        }
        if(s[i%2].empty()) cout << 0 << ' ';
    }
    return 0;
}
