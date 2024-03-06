# input
original=input()

escaped = original.encode('unicode-escape')
escaped = str(escaped)

intermediate = str('')

for i in range(len(escaped)):
    if i == 0:
        pass
    elif escaped[i] == '\'':
        pass
    elif escaped[i] == '\\':
        pass
    elif escaped[i] == 'u':
        pass
    else:
        intermediate += escaped[i]

# ブロック要素に変換
ans = str('')

for i in range(len(intermediate)):
    if intermediate[i] == '0':
        ans += '▐'
    elif intermediate[i] == '1':
        ans += '░'
    elif intermediate[i] == '2':
        ans += '▒'
    elif intermediate[i] == '3':
        ans += '▓'
    elif intermediate[i] == '4':
        ans += '▔'
    elif intermediate[i] == '5':
        ans += '▕'
    elif intermediate[i] == '6':
        ans += '▖'
    elif intermediate[i] == '7':
        ans += '▗'
    elif intermediate[i] == '8':
        ans += '▘'
    elif intermediate[i] == '9':
        ans += '▙'
    elif intermediate[i] == 'a':
        ans += '▚'
    elif intermediate[i] == 'b':
        ans += '▛'
    elif intermediate[i] == 'c':
        ans += '▜'
    elif intermediate[i] == 'd':
        ans += '▝'
    elif intermediate[i] == 'e':
        ans += '▞'
    elif intermediate[i] == 'f':
        ans += '▟'
    else:
        print('error!')

print('Conversion Result: ' + ans)
