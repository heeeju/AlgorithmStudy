#include <bits/stdc++.h>
#include <cstdlib>
using namespace std;

int cnt = 0;
int arr1[27];
int arr2[27];

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    string s1, s2;
    cin >> s1 >> s2;
    for(int i=0; i<s1.size(); i++){
        arr1[s1[i]-'a']++;
    }
    for(int i=0; i<s2.size(); i++){
        arr2[s2[i]-'a']++;
    }
    for(int i=0; i<26; i++){
        cnt += abs(arr1[i]-arr2[i]);
    }
    cout << cnt;
    return 0;
}
