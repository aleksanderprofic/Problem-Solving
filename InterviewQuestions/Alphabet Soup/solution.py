"""
Given a string of alphabetical characters following the rules seen down below in part A and part B
return a new string with the characters in alphabetical order. Capital letters should appear before the same
lowercase letters in part B. There will be no spaces in any of the strings.

Part A) The string contains only lowercase letters
Part B) The string contains both lowercase and uppercase letters

Sample Input/Output:
A) Input: 'hello', Output: 'ehllo'
B) Input: 'eLEPhAnt', Output: 'AEehLnPt'
"""

A = ord('A')
A_ = chr(A)

i = 1
key_dict = dict()

while A_ != 'Z':
    key_dict[A_] = i
    key_dict[A_.lower()] = i + 0.5
    A += 1
    A_ = chr(A)
    i += 1


def key_func(c: str):
    return key_dict[c]


def solution(string: str) -> str:
    return ''.join(sorted(string, key=key_func))


print(solution('eLEPhAnt'))
print(solution('bAaBbbAaAAABbABaa'))
print(solution('hello'))





