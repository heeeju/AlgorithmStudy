#include <bits/stdc++.h>
using namespace std;

//fill을 사용한 dp
//시간 초과
int dp[500001];

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int n;
    cin >> n;
    for(int i=1; i<=n; i++){
        int h; //height
        cin >> h;
        cout << dp[i] << ' ';
        fill(dp, dp+min(500000,h-1), i);
    }
    return 0;
}
