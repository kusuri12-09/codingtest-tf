#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	int blank = 0;
	char a[1000000];
	scanf("%[^\n]", a);

	if (strlen(a) == 1 && a[0] == ' ') {
		printf("%d", blank);

		return 0;
	}

	for (int i = 1; i < strlen(a) - 1; i++) {
		if (a[i] == ' ') {
			blank++;
		}
	}

	printf("%d", blank + 1);

	return 0;
}