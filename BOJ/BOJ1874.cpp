#include <bits/stdc++.h>
using namespace std;

stack<int> s;
int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int n;
    cin >> n;
    vector<int> seq;
    vector<char> ans;
    for(int i=0; i<n; i++){
        int temp;
        cin >> temp;
        seq.push_back(temp);
    }

    int idx=0;
    for(int i=1; i<=n; i++){
        s.push(i);
        ans.push_back('+');
        while(!s.empty()){
            if(s.top()!=seq[idx]) break;
            if(s.top()>seq[idx]){
                cout << "NO";
                return 0;
            }
            s.pop();
            ans.push_back('-');
            idx++;
        }
    }
    if(!s.empty()) {
        cout << "NO";
        return 0;
    }
    for(int i=0; i<ans.size(); i++)
        cout << ans[i] << '\n';
    return 0;
}
