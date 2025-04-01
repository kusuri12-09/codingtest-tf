#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int h1, m1, s1;
	int h2, m2, s2;

	scanf("%02d:%02d:%02d", &h1, &m1, &s1);
	scanf("%02d:%02d:%02d", &h2, &m2, &s2);

	if (s2 - s1 < 0) {
		m1++;
	}
	if (m2 - m1 < 0) {
		h1++;
	}
	if (h1 > h2) {
		h2 += 24;
	}
	if (m1 > m2) {
		m2 += 60;
	}
	if (s1 > s2) {
		s2 += 60;
	}

	printf("%02d:%02d:%02d", h2 - h1, m2 - m1, s2 - s1);
	return 0;

}