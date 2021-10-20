#include <bits/stdc++.h>
using namespace std;

list<char> l;
list<char>::iterator cur = l.begin();
void insert(char c){
    l.insert(cur, c);
}
void erase(){
    if(cur!=l.begin())
        cur = l.erase(--cur);
}
void moveL(){
    if(cur!=l.begin()) cur--;
}
void moveR(){
    if(cur!=l.end()) cur++;
}
void traversal(){
    for(auto c: l) cout << c;
    cout << "\n";
}
int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 
    
    int n;
    cin >> n;
    while(n--){
        string s;
        cin >> s;
        for(int i=0; i<s.size(); i++){
            if(s[i]=='<') moveL();
            else if(s[i]=='>') moveR();
            else if(s[i]=='-') erase();
            else{
                insert(s[i]);
            }
        }
        traversal();
        l.clear();
        cur = l.begin();
    }
    return 0;
}
