#include <bits/stdc++.h>
using namespace std;

//시간복잡도 (O lgN)
int func4(int N){
    int n = 1;
    for(int i=1; n<=N; i++){
        n *= 2;
    }
    return n/2;
}

//바킹독 코드
int func4_2(int N){
    int val = 1;
    while(2*val <=N) val *=2;
    return val;
}

int main(){
    int n; 
    cin >> n;
    cout << func4(n);
    return 0;
}