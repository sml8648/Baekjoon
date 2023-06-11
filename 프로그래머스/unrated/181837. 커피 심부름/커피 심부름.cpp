#include <iostream>
#include <string>
#include <vector>

int solution(std::vector<std::string> order) {
    int totalPrice = 0;
    
    for (const std::string& menu : order) {
        if (menu == "americano" || menu == "iceamericano" || menu == "americanoice" || menu == "anything") {
            totalPrice += 4500;
        } else if (menu == "cafelatte" || menu == "icecafelatte" || menu == "cafelatteice") {
            totalPrice += 5000;
        } else if (menu == "hotamericano" || menu == "americanohot") {
            totalPrice += 4500;
        } else if (menu == "hotcafelatte" || menu == "cafelattehot") {
            totalPrice += 5000;
        }
    }
    
    return totalPrice;
}