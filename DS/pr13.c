#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

void insertNode(struct Node **head, int data, int position)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;

    if (*head == NULL || position == 1)
    {
        newNode->next = *head;
        *head = newNode;
    }
    else
    {
        struct Node *prevNode = *head;
        for (int i = 1; i < position - 1; i++)
        {
            prevNode = prevNode->next;
        }

        newNode->next = prevNode->next;
        prevNode->next = newNode;
    }
}

int main()
{
    struct Node *head = NULL;
    insertNode(&head, 10, 1);
    insertNode(&head, 20, 2);
    insertNode(&head, 30, 3);

    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }

    return 0;
}
