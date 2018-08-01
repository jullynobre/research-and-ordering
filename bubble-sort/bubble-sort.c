#include <stdio.h>
#include <stdlib.h>

void swap(int *array, int n1, int n2) {
    int temp = array[n1];
    array[n1] = array[n2];
    array[n2] = temp;
}

void bubble_sort(int *array, int size) {
    int i;
    int isOrdenered = 0;
    while(!isOrdenered){
        isOrdenered = 1;
        for(i = 0; i < size - 1; i++) {
            if(array[i] > array[i + 1]){
                swap(array, i, i + 1);
                isOrdenered = 0;
            }
        } size--;
    }
}

int main() {
    int array[] = {3, 4, 1, 7, 4, 2, 5};
    int size = sizeof(array)/sizeof(array[0]);
    
    bubble_sort(array, size);
     
    int i;
    for(i = 0; i < size; i++){
        printf("%d\n", array[i]);
    }
    
    
    return 0;
}
