#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

int count_nodes(struct node *head)
{
    int count = 0;
    while (head != NULL)
    {
        count++;
        head = head->next;
    }
    return count;
}

int main()
{
    struct node *head = NULL;
    for (int i = 0; i < 10; i++)
    {
        struct node *new_node = (struct node *)malloc(sizeof(struct node));
        new_node->data = i;
        new_node->next = head;
        head = new_node;
    }

    int count = count_nodes(head);
    printf("The number of nodes in the linked list is %d\n", count);

    return 0;
}
