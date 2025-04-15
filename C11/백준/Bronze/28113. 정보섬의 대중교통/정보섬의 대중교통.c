#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int walk, bus, subway;
	scanf("%d %d %d", &walk, &bus, &subway);
	if (bus < subway) {
		printf("Bus");
	}
	else if (bus > subway) {
		printf("Subway");
	}
	else printf("Anything");

	return 0;
}