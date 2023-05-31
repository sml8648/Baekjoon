#include <string>
#include <vector>

using namespace std;

string solution(string myString) {
    string answer = "";
    for(auto chr : myString)
    {
        if(islower(chr))
        {
            answer += (char)((int)chr - 32);
        }
        else
        {
            answer += chr;
        }
    }
    return answer;
}