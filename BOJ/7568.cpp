#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main() {
    int N;
    cin >> N;
    vector <vector<int>> data;
    for(int i=0; i<N; i++){
        int a, b;
        cin >> a >> b;
        vector<int> v;
        v.push_back(a);
        v.push_back(b);
        data.push_back(v);
    }
    int rank[N];
    for(int i=0; i<N; i++){
        int count=1;
        for(int j=0; j<N; j++){
            if(i!=j){
                if(data[i][0]<data[j][0] && data[i][1] < data[j][1]){
                    count++;
                }
            }
        }
        rank[i]=count;
    }
    for(int i=0; i<N; i++){
        if(i!=0) cout << " ";
        cout << rank[i];
    }
}
