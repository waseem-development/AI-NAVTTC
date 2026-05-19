#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int stack[MAX];
int top = -1;

void push(int value) {
    if (top == MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = value;
}

void pop() {
    if (top == -1) {
        printf("Stack Underflow\n");
        return;
    }
    printf("Popped: %d\n", stack[top--]);
}

int peek() {
    if (top == -1) {
        printf("Stack is Empty\n");
        return -1;
    }
    return stack[top];
}

int isEmpty() {
    return top == -1;
}

void display() {
    if (top == -1) {
        printf("Stack is Empty\n");
        return;
    }
    printf("TOP\n");
    for (int i = top; i >= 0; i--)
        printf(" %d\n", stack[i]);
    printf("BOTTOM\n");
}

int main() {
    push(10);
    push(20);
    push(30);
    push(40);
    display();
    printf("Peek: %d\n", peek());
    pop();
    display();
    printf("Empty: %d\n", isEmpty());
    return 0;
}