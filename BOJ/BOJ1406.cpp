#include <bits/stdc++.h>
using namespace std;

int m;
const int MX = 600001;
int pre[MX];
char dat[MX];
int nxt[MX];
int cur = 0;
int unused=1;

void insert(char c){
    //현 데이터
    dat[unused] = c;
    //현 pre
    pre[unused] = cur;
    //현 nxt
    nxt[unused] = nxt[cur];
    //후 pre
    if(nxt[cur]!=-1) pre[nxt[cur]] = unused;
    //전 nxt
    nxt[cur] = unused;
    
    unused++;
    //커서 옮기기
    cur = nxt[cur];
}

void erase(){
    //전 nxt
    if(pre[cur]!=-1) { //앞에 아무것도 없으면 = (cur!=0)
    //if(cur != 0){
        nxt[pre[cur]]= nxt[cur];
        //후 pre
        if(nxt[cur]!=-1) pre[nxt[cur]] = pre[cur];
        //커서 옮기기
        cur = pre[cur];
    }
}

void moveL(){
    if(pre[cur] != -1) cur = pre[cur];
}

void moveR(){
    if(nxt[cur] !=-1) cur = nxt[cur];
}

void traverse(){
    int cur = nxt[0];
    while(cur !=-1){
        cout << dat[cur];
        cur = nxt[cur];
    }
}

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0); 

    fill(pre, pre+MX, -1);
    fill(nxt, nxt+MX, -1);

    string s;
    cin >> s;
    
    /*unused = s.size()+1;
    cur = s.size();

    nxt[0]=1;
    for(int i=1; i<=s.size(); i++){
        nxt[i-1] = i;
        pre[i] = i-1;
        dat[i]=s[i-1];
        //nxt[i] = i+1;
    }*/

    for(auto c : s) insert(c);

    cin >> m;
    
    while(m--){
        char c;
        cin >> c;
        if(c=='L') moveL();
        else if(c=='D') moveR();
        else if(c=='B') erase();
        else{
            char newC;
            cin >> newC;
            insert(newC);
        }
    }
    traverse();
    
}
