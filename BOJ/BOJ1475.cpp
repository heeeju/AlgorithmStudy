#include <bits/stdc++.h>
using namespace std;

int cnt[8];
int maxNum=0;

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    string s;
    cin >> s;
    for(int i=0; i<s.size(); i++){
        int idx = s[i]-'0';
        if(idx==9) idx=6;
        cnt[idx]++;

        int n = cnt[idx];
        if(idx==6) n = (n+1)/2;
        maxNum = max(n, maxNum);
    }
    cout << maxNum;
    return 0;
}
