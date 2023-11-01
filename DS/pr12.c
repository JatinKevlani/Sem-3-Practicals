#include <stdio.h>
#include <stdlib.h>

struct Node {
 int data;
 struct Node *next;
};

struct Node *head = NULL;

void insert(int data) {
 struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
 new_node->data = data;
 new_node->next = NULL;

 if (head == NULL) {
   head = new_node;
   return;
 }

 struct Node *current = head;
 while (current->next != NULL && current->data < data) {
   current = current->next;
 }

 if (current->data >= data) {
   new_node->next = current;
   head = new_node;
 } else {
   new_node->next = current->next;
   current->next = new_node;
 }
}

void print_list() {
 struct Node *current = head;
 while (current != NULL) {
   printf("%d ", current->data);
   current = current->next;
 }
 printf("\n");
}

int main() {
 insert(10);
 insert(20);
 insert(30);
 insert(40);
 insert(50);

 print_list();

 return 0;
}