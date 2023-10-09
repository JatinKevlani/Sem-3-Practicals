#include<stdio.h>
#include<string.h>

void convertLow(char *string){
    int i = 0;
    while(i < strlen(string)){
        if(string[i] >= 65 && string[i] <= 90)
            string[i] += 32;
        i++;
    }
}

int main(){
    char string[100];
    printf("Enter a string to convert into lower : ");
    gets(string);
    convertLow(string);
    printf("%s", string);
    return 0;
}