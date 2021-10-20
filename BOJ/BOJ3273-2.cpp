#include <bits/stdc++.h>
using namespace std;

int ans;

//시간초과
int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int n;
    int x;
    int arr[100001];

    cin >> n;
    for(int i=0; i<n; i++)
        cin >> arr[i];
    cin >> x;

    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            if(arr[i]+arr[j] == x) ans++;
        }
    }
    cout << ans;
    return 0;
}
