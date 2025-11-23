import sys
input = sys.stdin.readline
output = sys.stdout.write

n = input().strip()

output("YES" if n.startswith('555') else "NO")