#include<iostream>
using namespace std;
int main() {
    int a = 4, b = 5, temp;
    cout<<"Value of a: "<<a<<"\nValue of b: "<<b<<"\n";
    temp = a;
    a=b;
    b=temp;
    cout<<"Value of a: "<<a<<"\nValue of b: "<<b<<"\n";
    return 0;
}