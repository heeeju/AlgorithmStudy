#include <bits/stdc++.h>
using namespace std;

  int check[101];

//시간복잡도 O(N)
int func2(int arr[], int N){
  for(int i=0; i<N; i++){
    if(check[100-arr[i]]==1) return 1;
    check[arr[i]]=1;
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

    return 0;
}