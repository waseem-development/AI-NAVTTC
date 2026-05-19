#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int queue[MAX];
int front = -1;
int rear = -1;

void enqueue(int value) {
    if (rear == MAX - 1) {
        printf("Queue is Full\n");
        return;
    }
    if (front == -1)
        front = 0;
    queue[++rear] = value;
}

void dequeue() {
    if (front == -1) {
        printf("Queue is Empty\n");
        return;
    }
    printf("Dequeued: %d\n", queue[front++]);
    if (front > rear)
        front = rear = -1;
}

int peek() {
    if (front == -1) {
        printf("Queue is Empty\n");
        return -1;
    }
    return queue[front];
}

int isEmpty() {
    return front == -1;
}

void display() {
    if (front == -1) {
        printf("Queue is Empty\n");
        return;
    }
    printf("FRONT -> ");
    for (int i = front; i <= rear; i++)
        printf("%d -> ", queue[i]);
    printf("REAR\n");
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    display();
    printf("Peek: %d\n", peek());
    dequeue();
    display();
    printf("Empty: %d\n", isEmpty());
    return 0;
}