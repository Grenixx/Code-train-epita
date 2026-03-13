#include <stdlib.h>
#include <stdio.h>
struct Node{

    int elem;
    struct Node* racine;
    struct Node* fg;
    struct Node* fd;
};

int main(){
    struct Node racine; // dummy? 

    racine.elem = 3;
    struct Node* tail = &racine;
    
    for (int i = 0; i<3;i++){
        struct Node fg;
        fg.elem = 0;
        tail->fg = &fg;
        fg.racine = tail;
        tail = tail->fg; 
    }
    
    //printf("%d",tail->elem);
    //for (int i = 0;i<)
    return 0;
}