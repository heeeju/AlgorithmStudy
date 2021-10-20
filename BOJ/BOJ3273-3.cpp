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

    sort(arr, arr+n);

    for(int l=0, r=n-1; l<r;){
        if(arr[l]+arr[r] == x) {
            ans++;
            l++;
            r--;
        }
        else if(arr[l]+arr[r] < x) l++;
        else r--;
    }

    cout << ans;
    return 0;
}