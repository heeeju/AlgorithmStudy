#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 
    
    int check[27];
    fill(check, check+27, 0);

    string s;
    cin >> s;
    for(int i=0; i<s.size(); i++)
        check[s[i]-'a']++;
    
    for(int i=0; i<26; i++)
        cout << check[i] << ' ';

}
