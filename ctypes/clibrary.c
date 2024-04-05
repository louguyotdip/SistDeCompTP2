#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* display(char *str, int age){
    printf("Mi nombre es %s y mi edad es %d",str,age);
    return "completado";
}

char* alloc_memory(){
    //strdup es como malloc
    char* str=strdup("hola mundoo");
    printf("memoria alocada");
    return str;
}
void free_memory(char* ptr){
    printf("memoria desalcoada");
    free(ptr);
}


//matriz que recibe desde python
//le pasamos un puntero al array 
int sumArray(int *arr,int size){
    int sum =0;
    for(int i=0;i<size;i++){
        sum+=arr[i];
    }
    return sum;
}

int* incArray(int *arr,int size){
    for(int i=0;i<size;i++){
        arr[i]++;
    }
    return arr;
}