def decode_string_2(string):
    print(string)
    words = ['']
    nums = []
    num = 0
    prev = ''
    for s in string:
        if s.isdigit():
            num = int(s) + 10 * num

        elif s == '[':
            nums.append(num)
            words.append('')
            num = 0
        elif s == ']':
            repeater = nums.pop()
            word = words.pop()
            words.append(word * repeater)
        else:
            # if prev == '[':
            #     nums.append(1)
            curr_top = words.pop()
            curr_top += s
            words.append(curr_top)
        print(prev, s, nums, words)
        prev = s
    return words.pop()
    # letter - pop current word off stack, append and add back to stack
    # number - add to num stack
    # [ - create new empty level on stack
    # ] - multiply top word on stack by top num on stack, add to (new) current top word on stack


def decode_string(string):
    msg = ''
    num = 0
    depth = 0
    i = 0
    while i < len(string):
        s = string[i]
        if s.isdigit():
            num = 10 * num + int(s)
            print(f'n-i: {i} s:{s}, msg:{msg} depth:{depth} num:{num}')
            if string[i+1] == '[':
                depth += 1
                for j in range(i+2, len(string)):
                    print(f'j-loop str: {string[j]} i:{i} j:{j}, s:{s}, msg: {msg} depth:{depth} num:{num}')
                    if string[j] == '[':
                        depth += 1
                    if string[j] == ']':
                        depth -= 1
                    if depth == 0:
                        print(f'd0 i:{i}, j:{j}, str:{string[j]}')
                        print(f'calling {string[i+2:j]} * {num}')
                        msg += decode_string(string[i+2:j])*num
                        print(f'msg: {msg}')
                        num = 0
                        i = j
                        break

        else:
            print(f'adding {s}')
            msg += s
        print(f'l-i: {i} s:{s}, msg:{msg} depth:{depth} num:{num}')
        i += 1
    print(f'returning {msg}')
    return msg


print(decode_string('4[ab]'))
print('***************')
print(decode_string('2[b3[a]]'))
print('***************')
print(decode_string('z1[y]xzz2[abc]'))