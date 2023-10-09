#include<stdio.h>

int main(){
    int row, col;
    printf("Enter number of rows : ");
    scanf("%d", &row);
    printf("Enter number of columns : ");
    scanf("%d", &col);
    int mat[row][col];
    printf("Enter matrix elements :\n");
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            printf("Enter matrix[%d][%d]th element : ", i + 1, j + 1);
            scanf("%d", &mat[i][j]);
        }
    }
    printf("Row major :\n");
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
    printf("Column major :\n");
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            printf("%d ", mat[j][i]);
        }
        printf("\n");
    }
    return 0;
}