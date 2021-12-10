#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    string input[n];
    int count=0;
    for(int i=0; i<n; i++){
        cin >> input[i];
        bool total_check=true;
        bool check[26]={false};
        for(int j=0; j<input[i].size(); j++){
            if(j==input[i].size()-1){
                if(check[input[i][j]-'a']==true){
                    total_check=false;
                    break;
                }
            }
            else{
                if(input[i][j]!=input[i][j+1]){
                    if(check[input[i][j]-'a']==true){
                    total_check=false;
                    break;
                    }
                    else check[input[i][j]-'a']=true;
                }
            }
        }
        if(total_check) count++;
    }
    cout << count << endl;
}
