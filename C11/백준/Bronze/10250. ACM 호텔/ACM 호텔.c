#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int t;
	int h, w, n;
	int a, b;
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++) {
		scanf("%d %d %d", &h, &w, &n);
		a = n % h;
		b = n / h + 1;
		if (a == 0) {
			a = h;
			b--;
		}

		printf("%d\n", 100 * a + b);
	}

	return 0;
}