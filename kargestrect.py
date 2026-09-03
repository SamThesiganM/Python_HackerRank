#include<stdio.h>
int min(int *a, int s, int e){
    int i;
    int m = a[s];
    int ind = s;
    for(i = s; i < e; i++){
        if(a[i] < m){
            ind = i;
            m = a[i];
        }
    }
    return ind;
}
int m = 0;
int doit(int *a, int s, int e){
    if(s > e){
        return 0;
    }
    int k = e-s+1;
    int ind = min(a,s,e);
    int cur = k*a[ind];
    
    if(cur > m){
        m = cur;
    }
    doit(a,s,ind-1);
    doit(a,ind+1,e);
    return 0;
}
int main(){
    int size;
    scanf("%d",&size);
    int a[size];
    int i;
    for(i = 0; i < size; i++){
        scanf("%d",&a[i]);
    }
    doit(a,0,size-1);
    printf("%d\n",m);
}
