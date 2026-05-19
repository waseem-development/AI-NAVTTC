#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head = NULL;

struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

void insertAtEnd(int value) {
    struct Node* newNode = createNode(value);

    if (head == NULL) {
        head = newNode;
        return;
    }

    struct Node* temp = head;

    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
}

void insertAtStart(int value) {
    struct Node* newNode = createNode(value);
    newNode->next = head;
    head = newNode;
}

void insertAtPosition(int index, int value) {
    if (index == 0) {
        insertAtStart(value);
        return;
    }

    struct Node* newNode = createNode(value);
    struct Node* temp = head;

    for (int i = 0; i < index - 1; i++)
        temp = temp->next;

    newNode->next = temp->next;
    temp->next = newNode;
}

void display() {
    struct Node* temp = head;

    printf("HEAD -> ");

    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }

    printf("NULL\n");
}

int readAt(int index) {
    struct Node* temp = head;

    for (int i = 0; i < index; i++)
        temp = temp->next;

    return temp->data;
}

void update(int index, int value) {
    struct Node* temp = head;

    for (int i = 0; i < index; i++)
        temp = temp->next;

    temp->data = value;
}

void deleteAt(int index) {
    if (index == 0) {
        struct Node* temp = head;
        head = head->next;
        free(temp);
        return;
    }

    struct Node* temp = head;

    for (int i = 0; i < index - 1; i++)
        temp = temp->next;

    struct Node* toDelete = temp->next;
    temp->next = toDelete->next;

    free(toDelete);
}

int main() {
    insertAtEnd(10);
    insertAtEnd(20);
    insertAtEnd(30);
    insertAtEnd(40);
    insertAtEnd(50);

    display();

    insertAtStart(5);
    display();

    insertAtPosition(3, 99);
    display();

    update(3, 77);
    display();

    deleteAt(3);
    display();

    printf("%d\n", readAt(2));

    return 0;
}