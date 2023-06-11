#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string overwrite_string, int s) {
    string answer = "";
    for(int i = 0; i < my_string.length(); i++)
    {
        answer += my_string[i];
    }
    for(int i = 0; i < overwrite_string.length();i++)
    {
        answer[s+i] = overwrite_string[i];
    }
    return answer;
}