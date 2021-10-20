#include <bits/stdc++.h>
using namespace std;

int ans;
stack<int> s;
int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int k;
    cin >> k;
    for(int i=0; i<k; i++){ //이거를 while(k--)로 하는 습관 들이기!!
        int n; 
        cin >> n;
        if(n==0) s.pop();
        else s.push(n);
    }

    while(!s.empty()){
        ans+=s.top();
        s.pop();
    }

    cout << ans;
}
