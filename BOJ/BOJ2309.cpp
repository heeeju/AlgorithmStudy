#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    int height[9];
    int sum=0;
    for(int i=0; i<9; i++){
        cin >> height[i];
        sum += height[i];
    }
    sum -= 100;
    sort(height, height+9);

    for(int l=0, r=8; l<r; ){
        if(height[l]+height[r] == sum){
            height[l] = 0;
            height[r] = 0;
        } 
        else if(height[l]+height[r] < sum) l++;
        else r--;
    }

    for(int i=0; i<9; i++)
        if(height[i] != 0) cout << height[i] << '\n';
}