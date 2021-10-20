#include <bits/stdc++.h>
using namespace std;
const int MAX = 5001;
int pre[MAX];
int dat[MAX];
int nxt[MAX];
int unused=1;
int cur = 0;
int isFirst = 1;
int check = 1;

void insert(int num){
    dat[unused] = num;
    pre[unused] = cur;
    nxt[unused] = nxt[cur];
    if(nxt[cur]!=-1) pre[nxt[cur]] = unused;
    nxt[cur] = unused;

    cur = unused;
    unused++;
}
void erase(){
    if(dat[cur]==dat[nxt[cur]]) check=0;
    if(isFirst){
        cout << "<" << dat[cur];
        isFirst = false;
    }
    else cout << ", " << dat[cur];
    nxt[pre[cur]] = nxt[cur];
    if(nxt[cur] !=-1) pre[nxt[cur]] = pre[cur];

}
void move(){
    cur = nxt[cur];
}

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    fill(pre, pre+MAX, -1);
    fill(nxt, nxt+MAX, -1);

    nxt[0]=1;

    //리스트 초기화
    int N, K, k;
    cin >> N >> K;
    for(int i=1; i<=N; i++) insert(i);

    //원형
    nxt[N]=1;

    //반복
    while(check){
        k = K;
        while(k--){
            move();
        }
        erase();
    }
    cout << '>';
    return 0;
}
