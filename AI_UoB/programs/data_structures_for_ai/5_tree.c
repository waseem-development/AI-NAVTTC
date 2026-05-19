#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

struct Node* insert(struct Node* root, int value) {
    if (root == NULL)
        return createNode(value);
    if (value < root->data)
        root->left = insert(root->left, value);
    else if (value > root->data)
        root->right = insert(root->right, value);
    return root;
}

struct Node* search(struct Node* root, int value) {
    if (root == NULL || root->data == value)
        return root;
    if (value < root->data)
        return search(root->left, value);
    else
        return search(root->right, value);
}

struct Node* findMinimum(struct Node* root) {
    while (root->left != NULL)
        root = root->left;
    return root;
}

struct Node* delete(struct Node* root, int value) {
    if (root == NULL)
        return root;
    if (value < root->data)
        root->left = delete(root->left, value);
    else if (value > root->data)
        root->right = delete(root->right, value);
    else {
        // Case 1 — no children
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        }
        // Case 2 — one child
        else if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }
        // Case 3 — two children
        else {
            struct Node* temp = findMinimum(root->right);
            root->data = temp->data;
            root->right = delete(root->right, temp->data);
        }
    }
    return root;
}

// Left → Root → Right
void inorder(struct Node* root) {
    if (root == NULL)
        return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

// Root → Left → Right
void preorder(struct Node* root) {
    if (root == NULL)
        return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

// Left → Right → Root
void postorder(struct Node* root) {
    if (root == NULL)
        return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

int main() {
    struct Node* root = NULL;
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 70);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 60);
    root = insert(root, 80);

    printf("Inorder:   "); inorder(root);   printf("\n");
    printf("Preorder:  "); preorder(root);  printf("\n");
    printf("Postorder: "); postorder(root); printf("\n");

    struct Node* found = search(root, 40);
    printf("Search 40: %s\n", found ? "Found" : "Not Found");

    root = delete(root, 30);
    printf("After deleting 30: "); inorder(root); printf("\n");

    return 0;
}