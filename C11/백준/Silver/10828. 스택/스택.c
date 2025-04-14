#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int top = -1;
int stack[10000];

int is_empty() {
	if (top == -1) {
		return 1;
	}
	else return 0;
}

void push(int num) {
	top++;
	stack[top] = num;
}

int pop() {
	if (is_empty()==0) {
		int value = stack[top];
		top--;
		return value;
	}
	else return -1;
}

int size() {
	int size = top + 1;
	return size;
}

int main() {
	int num;
	int x;
	char str[6];
	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%s", str);
		if (strcmp(str, "pop") == 0) {
			printf("%d\n", pop());
		}
		else if (strcmp(str, "push") == 0) {
			scanf("%d", &x);
			push(x);
		}
		else if (strcmp(str, "top") == 0) {
			if (top == -1) {
				printf("%d\n", -1);
			}
			else printf("%d\n", stack[top]);
		}
		else if (strcmp(str, "size") == 0) {
			printf("%d\n", size());
		}
		else if (strcmp(str, "empty") == 0) {
			printf("%d\n", is_empty());
		}
	}
	return 0;
}