#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int num[9];
	int max = 0, seq;

	for (int i = 0; i < 9; i++) {
		scanf("%d", &num[i]);
	}

	for (int i = 0; i < 9; i++) {
		if (num[i] > max) {
			max = num[i];
			seq = i + 1;
		}
	}

	printf("%d\n", max);
	printf("%d\n", seq);

	return 0;
}