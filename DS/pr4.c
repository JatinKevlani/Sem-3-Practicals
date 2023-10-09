#include<stdio.h>

int binarySearch(int arr[], int size, int key){
    int start = 0;
    int end = size - 1;
    while(start <= end){
        int mid = (start + end) / 2;
        if(arr[mid] > key)
            end = mid - 1;
        else if(arr[mid] < key)
            start = mid + 1;
        else
            return mid;
    }
    return -1;
}

int main(){
    int size;
    printf("Enter the size of the array : ");
    scanf("%d", &size);
    int arr[size];
    printf("Enter the elements of the array in ascending order :\n");
    for(int i = 0; i < size; i++)
        scanf("%d", &arr[i]);
    int key;
    printf("Enter the element you want to search : ");
    scanf("%d", &key);
    int binSearch = binarySearch(arr, size, key);
    if(binSearch == -1)
        printf("Element not found!");
    else
        printf("Element found at %dth position.", binSearch + 1);
    return 0;
}