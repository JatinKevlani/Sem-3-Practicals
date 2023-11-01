#include <stdio.h>

struct Person {
    char name[50];
    int age;
};

int main() {
    struct Person person1;
    struct Person *ptrPerson = &person1;
    printf("Enter name: ");
    scanf("%s", ptrPerson->name);
    printf("Enter age: ");
    scanf("%d", &ptrPerson->age);
    printf("\nPerson Information:\n");
    printf("Name: %s\n", ptrPerson->name);
    printf("Age: %d\n", ptrPerson->age);
    return 0;
}