#include <bits/stdc++.h>
using namespace std;

int func3(int N){
    for(int i=1; i<=N; i++){
        if(i*i == N) return 1;
        else if(i*i > N) return 0;
    }
    return 0;
}

//좀 더 좋은 코드 -> 시간복잡도 O(루트N)
int func3_2(int N){
    for(int i=1; i*i <= N; i++){
        if(i*i == N) return 1;
    }
    return 0;
}

int main(){
    int n; 
    cin >> n;
    cout << func3(n);
    return 0;
}