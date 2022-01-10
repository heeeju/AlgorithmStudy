#include <bits/stdc++.h>
using namespace std;

stack< vector<int> > s; //높이와 인덱스

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int n;
    cin >> n;
    for(int i=1; i<=n; i++){
        int h;
        cin >> h;
        while(!s.empty()){
            if(s.top()[0]>h){
                cout << s.top()[1] << ' ';
                break;
            }
            s.pop();
        }
        if(s.empty()) cout << 0 << ' ';
        vector<int> v;
        v.push_back(h);
        v.push_back(i);
        s.push(v);
    }
    return 0;
}
