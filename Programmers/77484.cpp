#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    sort(lottos.begin(), lottos.end());
    sort(win_nums.begin(), win_nums.end());
    int cnt = 0, cnt_zero = 0;
    for(int i=0, j=0; i<6 && j<6;){
        if(lottos[i] < win_nums[j]){
            if(lottos[i]==0) cnt_zero ++;
            i++;
        }
        else if(lottos[i] > win_nums[j]){
            j++;
        }
        else{
            cnt++;
            i++;
            j++;
        }
    }
    answer.push_back(min(6 ,7-(cnt + cnt_zero)));
    answer.push_back(min(6, 7-cnt));
    return answer;
}
