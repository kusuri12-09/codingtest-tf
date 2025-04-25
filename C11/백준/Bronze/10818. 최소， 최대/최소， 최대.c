#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int num;
	int numArr[1000000];
	int numMax = -1000000, numMin = 1000000;
	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%d", &numArr[i]);
		if (numMax < numArr[i]) {
			numMax = numArr[i];
		}
		if (numMin > numArr[i]) {
			numMin = numArr[i];
		}
	}

	printf("%d %d", numMin, numMax);

	return 0;
}