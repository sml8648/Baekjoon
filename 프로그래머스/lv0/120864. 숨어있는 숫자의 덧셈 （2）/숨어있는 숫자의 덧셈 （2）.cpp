#include <iostream>
#include <string>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    int num = 0;
    for(int i=0; i<my_string.size(); i++){
        if(isdigit(my_string[i])){ // 현재 문자가 숫자인 경우
            num = num*10 + (my_string[i]-'0'); // 숫자를 만들어감
        }
        else{ // 현재 문자가 숫자가 아닌 경우
            answer += num; // 숫자 합에 추가
            num = 0; // 숫자 초기화
        }
    }
    answer += num; // 마지막 숫자 합에 추가
    return answer;
}