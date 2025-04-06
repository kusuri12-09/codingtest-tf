#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	char quiz[80];
	for (int i = 0; i < n; i++) {
		scanf("%s", quiz);
		int sequ = 0;
		int score = 0;
		for (int j = 0; quiz[j] != '\0'; j++) {
			if (quiz[j] == 'O') {
				sequ++;
				score += sequ;
			}
			else sequ = 0;
		}
		printf("%d\n", score);
	}

}