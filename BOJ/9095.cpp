#include <bits/stdc++.h>
using namespace std;

int main(){
  int dp[11];
  int T;
  cin >> T;
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;
  while(T--){
    int n;
    cin >> n;
    for(int i=4; i<=n; i++){
      dp[i] = dp[i-1]+dp[i-2]+dp[i-3];
    }
    cout << dp[n] << endl;
  }
  return 0;
}
