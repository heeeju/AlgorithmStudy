#include <bits/stdc++.h>
using namespace std;

list<char> l;
list<char>::iterator cur = l.begin();
void insert(char c){
    l.insert(cur, c);
}
void erase(){
    if(cur != l.begin()) cur = l.erase(--cur); 
}
void moveL(){
    if(cur != l.begin()) cur--;
}
void moveR(){
    if(cur != l.end()) cur++;
}
void traversal(){
    for(auto c : l) cout << c;
}

//STL LIST 사용하여 풀어보기
int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0);     

    string s;
    cin >> s;
    int m;
    cin >> m;

    for(auto c : s){
        insert(c);
    }

    while(m--){
      char op;
      cin >> op;
      if(op=='L'){
          moveL();
      }
      else if(op=='D'){
          moveR();
      }
      else if(op=='B'){
          erase();
      }
      else{
        char c;
        cin >> c;
        insert(c);
      }
    }
    traversal();
    return 0;
}
