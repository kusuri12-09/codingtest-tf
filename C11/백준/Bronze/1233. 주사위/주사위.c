#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	/*주사위 3개*/
	/*각각 s1, s2, s3개의 면이 있다*/
	/*가장 높은 빈도로 나오는 합 구하기*/
	/*ex) 3 2 3 입력할 경우, 5출력 */
	/*(주사위 눈의 합의 모든 경우의 수 중 가장 높은 빈도)*/
	int s1, s2, s3;
	scanf("%d %d %d", &s1, &s2, &s3);
	int max = s1 + s2 + s3;
	int num[100] = {0};
	int i, j, k; /*i는 s1 j는 s2 k는 s3*/
	for (i = 1; i <= s1; i++) {
		for (j = 1; j <= s2; j++) {
			for (k = 1; k <= s3; k++) {
				num[i + j + k]++;
			}
		}
	}

	int freq = 0, result = 0;
	for (int i = 3; i <= max; i++) {
		if (num[i] > freq) {
			freq = num[i];
			result = i;
		}
	}

	printf("%d", result);

	return 0;
}