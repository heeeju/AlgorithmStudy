#include <bits/stdc++.h>
using namespace std;

//시간복잡도 O(N^2)
int func2(int arr[], int N){
    for(int i=0; i<N-1; i++){
        for(int j=i+1; j<N; j++){
            if(arr[i] + arr[j] == 100)
                return 1;
        }
    }
    return 0;
}

//시간복잡도 O(N)
int func2_2(int arr[], int N){
    sort(arr, arr+N);
    for(int l=0, r=N-1; l<r;){
        if(arr[l] + arr[r] < 100)
            l++;
        else if(arr[l] + arr[r] == 100) return 1;
        else r--;
    }
    return 0;
}

int main(){
    int n, i;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    cout << func2(arr, n);
    cout << func2_2(arr, n);

    return 0;
}