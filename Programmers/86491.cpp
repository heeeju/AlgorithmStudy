#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int max = sizes[0][0];
    int max2 = 0;
    int max_idx = 0;
    for(int i=0; i<sizes.size(); i++){
        for(int j=0; j<2; j++){
            if(max < sizes[i][j]){
                max = sizes[i][j];
                max2 = sizes[i][(j+1)%2];
                max_idx = j;
            }
        }
    }
    int idx = (max_idx+1) % 2;
    for(int i=0; i<sizes.size(); i++){
        if(sizes[i][max_idx] < sizes[i][idx]){
            int buf = sizes[i][max_idx];
            sizes[i][max_idx] = sizes[i][idx];
            sizes[i][idx] = buf;
        }
        if(max2 < sizes[i][idx]){
            max2 = sizes[i][idx];
        }
    }
    answer = max * max2;

    return answer;
}
