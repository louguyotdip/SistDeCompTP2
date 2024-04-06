#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
    Esta funcion transforma de tipo float a tipo int y le suma 1 
    a cada elemento de la array proveniente del codigo en python 
    @param arr :arreglo con los indices gini
    @param size :tamaño del arreglo
*/
int* ChangesArray(float *arr,int size){
    int* array_int = malloc(size * sizeof(int));
    for(int i=0;i<size;i++){
        array_int[i]=(int)arr[i];
        array_int[i]++;
    }
    return array_int;
}

void free_memory(int *arr){
    free(arr);
}
