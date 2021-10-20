#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    long long a, b, temp;
    cin >> a >> b;
    
    if(a>b){
        temp = a;
        a = b;
        b = temp;
    }

    if(a==b) cout << 0;
    else cout << b-a-1;
    cout << '\n';

    a++;
    for(; a<b; a++){
        cout << a << ' ';
    }
    return 0;
}
