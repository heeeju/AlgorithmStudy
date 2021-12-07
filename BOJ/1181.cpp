#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
using namespace std;
bool compare(string a,string b){
    if(a.size()==b.size()) return a<b;
    else return a.size()<b.size();
}

int main() {
    int num;
    cin >> num;
    set<string> results;
    vector<string> words;
    while(num--){
        string word;
        cin >> word;
        results.insert(word);
    }
    for (auto it= results.begin(); it!= results.end(); it++)
        words.push_back(*it);
    sort(words.begin(),words.end(), compare);
    for(int i=0; i<words.size(); i++)
        cout << words[i] << endl;
}
