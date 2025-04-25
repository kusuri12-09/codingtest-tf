#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int num;
	int input;
	int numMax = -1000000, numMin = 1000000;
	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%d", &input);
		if (numMax <= input) {
			numMax = input;
		}
		if (numMin >= input) {
			numMin = input;
		}
	}

	printf("%d %d", numMin, numMax);

	return 0;
}