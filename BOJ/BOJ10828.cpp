#include <bits/stdc++.h>
#include <stdlib.h>
using namespace std;

stack<int> s;

void push(int x){
    s.push(x);
}

void pop(){
    if(s.empty()){
        cout << -1 << '\n';
    }
    else{
        cout << s.top() << '\n';
        s.pop();
    }
}

void size(){
    cout << s.size() << '\n';
}

void empty(){
    if(s.empty()) cout << 1 << '\n';
    else cout << 0 << '\n';
    //cout << (int)s.empty() << '\n'; 써도됨
}

void top(){
    if(s.empty()) cout << -1 << '\n';
    else cout << s.top() << '\n';
}

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        string s;
        cin >> s;
        if(s=="push"){
            int x;
            cin >> x;
            push(x);
        }
        else if(s=="pop") pop();
        else if(s=="size") size();
        else if(s=="empty") empty();
        else if(s=="top") top();
    }
    return 0;
}
