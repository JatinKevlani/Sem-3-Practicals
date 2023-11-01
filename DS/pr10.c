#include <stdio.h>
#include <stdlib.h>

struct Node {
 int data;
 struct Node *next;
};

struct Node *head = NULL;

void insertAtBeginning(int data) {
 struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
 newNode->data = data;
 newNode->next = head;
 head = newNode;
}

void printList() {
 struct Node *temp = head;
 while (temp != NULL) {
   printf("%d ", temp->data);
   temp = temp->next;
 }
 printf("\n");
}

int main() {
 insertAtBeginning(10);
 insertAtBeginning(20);
 insertAtBeginning(30);
 printList();
 return 0;
}