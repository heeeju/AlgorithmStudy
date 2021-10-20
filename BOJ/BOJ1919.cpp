#include <bits/stdc++.h>
using namespace std;

int cnt = 0;
int arr[27];

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    string s1, s2;
    cin >> s1 >> s2;
    for(int i=0; i<s1.size(); i++){
        arr[s1[i]-'a']++;
        cnt++;
    }
    for(int i=0; i<s2.size(); i++){
        if(arr[s2[i]-'a']==0){
            cnt++;
        }
        else {
            arr[s2[i]-'a']--;
            cnt--;
        }
    }
    cout << cnt;
    return 0;
}
