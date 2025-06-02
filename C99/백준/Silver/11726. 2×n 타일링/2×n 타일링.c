//
// Created by user on 25. 6. 2.
//
#include <stdio.h>

int fibonacci(int n) {
    int f[n];
    f[0] = 1;
    f[1] = 1;
    if(n == 1 || n == 0){
        return 1;
    }
    else{
        for(int i = 2; i <= n; i++){
            f[i] = (f[i-1] + f[i-2])%10007;
        }
        return f[n];
    }
}

int main(void){
    int n;
    scanf("%d", &n);

    printf("%d", fibonacci(n)%10007);
    return 0;
}