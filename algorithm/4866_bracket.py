def check_bracket(words):
    stack = []
    top = -1
    for word in words:
        if word == '(':  # 열린 소괄호
            stack.append('(')
            top += 1
        elif word == '{':  # 열린 중괄호
            stack.append('{')
            top += 1
        elif (word == ')' or word == '}') and top <= -1:  # 아무것도 없는데 닫힌 소괄호 들어오는 경우
            return 0
        elif word == ')' and stack[top] == '(':  # 닫힌 소괄호 들어오면서 짝이 맞는 경우
            stack.pop()
            top -= 1
        elif word == ')' and stack[top] != '(':  # 닫힌 소괄호 들어오면서 안맞는 경우
            return 0
        elif word == '}' and stack[top] == '{':  # 닫힌 소괄호 들어오면서 짝이 맞는 경우
            stack.pop()
            top -= 1
        elif word == '}' and stack[top] != '{':  # 닫힌 소괄호 들어오면서 안맞는 경우
            return 0
        else:  # 괄호 아닌 다른 문자 들어오는 경우
            pass

    if not stack:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    words = input()

    result = check_bracket(words)

    print(f'#{tc}', result)
