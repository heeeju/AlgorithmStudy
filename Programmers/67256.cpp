#include <string>
#include <vector>

using namespace std;
int abs(int n){
    if(n > 0) return n;
    else return -n;
}
string solution(vector<int> numbers, string hand) {
    string answer = "";
    int l = 10, r = 12;
    for(int n:numbers){
        if(n==0) n = 11;
        if(n == 1 || n == 4 || n == 7){
            answer += 'L';
            l = n;
        }
        else if(n == 3 || n == 6 || n == 9){
            answer += 'R';
            r = n;
        }
        else{
            int l_n = abs((n-1)/3 - (l-1)/3) + abs((n-1)%3 - (l-1)%3);
            int r_n = abs((n-1)/3 - (r-1)/3) + abs((n-1)%3 - (r-1)%3);
            if(l_n > r_n){
                answer += 'R';
                r = n;
            }
            else if(l_n < r_n){
                answer += 'L';
                l = n;
            }
            else{
                answer += hand[0] - 'a' + 'A';
                if(hand[0] == 'l') l = n;
                else r = n;
            }
        }
    }
    return answer;
}
