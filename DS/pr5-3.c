#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char *concatStr(char str1[], char str2[]){
    int i;
    char *newStr = malloc(strlen(str1) + strlen(str2) + 1);
    for(i = 0; i < strlen(str1); i++)
        newStr[i] = str1[i];
    for(int j = 0; j < strlen(str2); j++, i++)
        newStr[i] = str2[j];
    newStr[i] = '\0';
    return newStr;
}

int main(){
    char str1[100];
    printf("Enter string 1 : ");
    gets(str1);
    char str2[100];
    printf("Enter string 2 : ");
    gets(str2);
    char *newStr = concatStr(str1, str2);
    printf("%s", newStr);
    return 0;
}