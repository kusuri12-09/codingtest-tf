#include <stdio.h>
#define min(A,B) A<B?A:B

int fibonacci(int n) {
    int f[1000000];

    for(int i = 2; i <= n; i++){
        f[i] = f[i-1] + 1;

        if (i%2 == 0) {
           f[i] = min(f[i/2]+1, f[i]);
        }

        if (i%3 == 0) {
            f[i] = min(f[i/3]+1, f[i]);
        }
    }
    return f[n];

}

int main(void){
    int n;
    scanf("%d", &n);

    printf("%d", fibonacci(n));
    
    return 0;
}