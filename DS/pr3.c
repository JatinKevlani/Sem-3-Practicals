#include <stdio.h>

int main()
{
    int size;
    printf("Enter size of the array : ");
    scanf("%d", &size);
    printf("Enter elements of the array :\n");
    int arr[size];
    for(int i = 0; i < size; i++){
        scanf("%d", &arr[i]);
    }
    int key;
    int flag = 0;
    printf("Enter the elemnent you want to find : ");
    scanf("%d", &key);
    int pos;
    for(int i = 0; i < size; i++){
        if(arr[i] == key){
            printf("Element is found at %dth position.", i+1);
            return 0;
        }
    }
    printf("Element not found!");
    return 0;
}