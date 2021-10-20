#include <bits/stdc++.h>
using namespace std;

int cnt[2000001];
int arr[100001];
int ans;

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int n;
    int x;

    cin >> n;
    for(int i=0; i<n; i++)
        cin >> arr[i];
    cin >> x;

    for(int i=0; i<n; i++){
        if(cnt[x-arr[i]]==1) ans++;
        cnt[arr[i]]= 1;
    }
    cout << ans;
    return 0;
}
