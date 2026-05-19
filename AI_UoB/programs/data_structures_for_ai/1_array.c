#include <stdio.h>

int arr[100] = {10, 20, 30, 40, 50};
int size = 5;

void insertAtEnd(int value) {
    arr[size] = value;
    size++;
}

void insertAtPosition(int index, int value) {
    for (int i = size; i > index; i--)
        arr[i] = arr[i - 1];
    arr[index] = value;
    size++;
}

void display() {
    printf("{");
    for (int i = 0; i < size; i++) {
        if (i == size - 1)
            printf("%d", arr[i]);
        else
            printf("%d, ", arr[i]);
    }
    printf("}\n");
}

int readAt(int index) {
    return arr[index];
}

void update(int index, int value) {
    arr[index] = value;
}

void deleteAt(int index) {
    for (int i = index; i < size - 1; i++)
        arr[i] = arr[i + 1];
    size--;
}

int main() {
    display();
    insertAtEnd(60);
    display();
    insertAtPosition(2, 99);
    display();
    update(2, 77);
    display();
    deleteAt(2);
    display();
    printf("%d\n", readAt(1));
    return 0;
}