#include <iostream>
#include <string>
using namespace std;

int main() {
    int size;
    cin >> size;
    int cnt[26]={0};
    bool success = false;
    string name[size];
    for(int i=0; i<size; i++){
        cin >> name[i];
        cnt[name[i][0]-'a']++;
    }
    for(int i=0; i<26; i++)
        if(cnt[i]>=5){
            char result = i+'a';
            cout << result;
            success = true;
        }
    if(!success) cout << "PREDAJA";
}
