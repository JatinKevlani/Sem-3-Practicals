#include <stdio.h>

int findSum(const int *arr, int size) {
    int sum = 0;
        for (int i = 0; i < size; i++) {
        sum += *arr;
        arr++;
    }

    return sum;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    int sum = findSum(arr, size);
    printf("Sum of the elements: %d\n", sum);
    return 0;
}