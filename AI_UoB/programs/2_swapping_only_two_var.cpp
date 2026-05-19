#include<iostream>
using namespace std;
int main() {
    int a = 4, b = 5;
    cout<<"Value of a: "<<a<<"\nValue of b: "<<b<<"\n";

    a = a + b;
    b = a - b;
    a = a - b;

    cout<<"Value of a: "<<a<<"\nValue of b: "<<b<<"\n";
    return 0;
}