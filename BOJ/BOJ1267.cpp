#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int n;
    int arr[21];
    cin >> n;
    int y=0, m=0;
    for(int i=0; i<n; i++){
        int t;
        cin >> t;
        y += (t/30+1) * 10;
        m += (t/60+1) * 15;
    }
    if(y==m) cout << "Y M " << y;
    else if(y<m) cout << "Y " << y;
    else cout << "M " << m;

    return 0;
}
