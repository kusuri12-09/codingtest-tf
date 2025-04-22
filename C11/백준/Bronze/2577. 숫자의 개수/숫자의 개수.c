#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int A, B, C;
	int result;
	int arr[10] = { 0 };
	scanf("%d %d %d", &A, &B, &C);

	result = A * B * C;
	
	for (int i = 0; result > 0; i++) {
		int digit = result % 10;
		arr[digit]++;
		result /= 10;
	}

	for (int i = 0; i < 10; i++) {
		printf("%d\n", arr[i]);
	}

	return 0;
}