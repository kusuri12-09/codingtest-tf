#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n, k;
	int a[10];
	int result = 0;
	scanf("%d %d", &n, &k);
	for (int i = 0; i < 10; i++) {
		scanf("%d", &a[i]);
	}
	for (int i = n - 1; i >= 0; i--) {
		while (k >= a[i]) {
			result++;
			k -= a[i];
		}
	}
	printf("%d", result);

}