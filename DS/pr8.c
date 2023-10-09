#include<stdio.h>
#include<stdlib.h>

int size, front = -1, rear = -1;

void display(int queue[]){
    if(front == -1){
        printf("Queue is empty\n");
        return;
    }
    printf("Queue :\n");
    for(int i = front; i <= rear; i++)
        printf("%d\n", queue[i]);
}

void push(int queue[]){
    if(rear == size - 1){
        printf("Queue is full\n");
        return;
    }
    if(front == -1)
        front++;
    rear++;
    int element;
    printf("Enter the element you want to insert : ");
    scanf("%d", &element);
    queue[rear] = element;
    printf("%d inserted\n", queue[rear]);
}

void pop(int queue[]){
    if(front == -1){
        printf("Queue is empty\n");
        return;
    }
    printf("%d popped\n", queue[front]);
    if(front == rear){
        front = -1;
        rear = -1;
    }
    else{
        front++;
    }
}

int main(){
    printf("Enter size of the queue : ");
    scanf("%d", &size);
    int queue[size];
    while(1){
        int choice;
        printf("1. Push\n2. Pop\n3. Display\n4. Exit\n");
        printf("Enter your choice : ");
        scanf("%d", &choice);
        switch(choice){
            case 1 : push(queue);
                     break;
            case 2 : pop(queue);
                     break;
            case 3 : display(queue);
                     break;
            case 4 : exit(0);
            default : printf("Invalid choice\n");
        }
    }
    return 0;
}