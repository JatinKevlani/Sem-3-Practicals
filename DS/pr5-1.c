#include<stdio.h>
#include<string.h>

int findLen(char string[]){
    int i = 0;
    while(string[i] != '\0')
        i++;
    return i;
}

int main(){
    char string[100];
    printf("Enter a string : ");
    gets(string);
    printf("Length of the string is : %d", findLen(string));
    return 0;
}