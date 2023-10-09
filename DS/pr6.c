#include<stdio.h>
#include<stdlib.h>

int size;
int top = -1;

void display(int stack[]){
    if(top == -1){
        printf("Stack is empty\n");
        return;
    }
    printf("Stack :\n");
    for(int i = top; i >= 0; i--){
        printf("%d\n", stack[i]);
    }
}

void push(int stack[]){
    if(top >= size - 1){
        printf("Stack is full\n");
        return;
    }
    top++;
    int item;
    printf("Enter the element you want to insert : ");
    scanf("%d", &item);
    stack[top] = item;
}

void pop(int stack[]){
    if(top == -1){
        printf("Stack is empty\n");
        return;
    }
    printf("%d popped\n", stack[top]);
    top--;
}

int main(){
    printf("Enter the size of the stack : ");
    scanf("%d", &size);
    int stack[size];
    int choice;
    while(1){
        printf("1.Push\n2.Pop\n3.Display\n4.Exit\n");
        printf("Enter your choice : ");
        scanf("%d", &choice);
        switch(choice){
            case 1 : push(stack);
                     break;
            case 2 : pop(stack);
                     break;
            case 3 : display(stack);
                     break;
            case 4 : exit(0);
            default : printf("Invalid choice\n");
        }
    }
    return 0;
}