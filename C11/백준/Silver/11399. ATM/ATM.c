#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int people;
	int time[1000];
	int temp = 0;
	int result = 0;

	scanf("%d", &people);
	for (int i = 0; i < people; i++) {
		scanf("%d", &time[i]);
	}

	for (int i = 0; i < people - 1; i++) {
		for (int j = 0; j < people - 1 - i; j++) {
			if (time[j] > time[j + 1]) {
				temp = time[j];
				time[j] = time[j + 1];
				time[j + 1] = temp;
			}
		}
	}

	for (int i = 0; i < people; i++) {
		for (int j = 0; j <= i; j++) {
			result += time[j];
		}
	}
	printf("%d", result);
	
	return 0;
}