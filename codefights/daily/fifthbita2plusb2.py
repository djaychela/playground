def fifthBitA2PlusB2(a, b):
    sum = a*a + b*b
    output = bin(sum)[-6]
    return output


tests = [ (251129265 , 673395586 , 1),
          (105198459, 805822999, 1),
          (717757366, 213356038, 0),
          (138127119, 369545330, 1),
          (190352610, 593431801, 1),
          (826921131, 48669151, 1),
          (725660770, 667662425, 1),
          (380307315, 524023846, 0)]


run_true = True
for idx, test in enumerate(tests, 1):
    a, b, answer = test
    result = int(fifthBitA2PlusB2(a, b))
    if run_true and not (answer == result):
        run_true = False
    print(f"{idx}: a = {a}, b = {b}, answer = {answer},"
          f" func:{result} func={answer == result} ")
if run_true:
    print(f"Success - STOP THE CLOCK!")


# print(bin(a))
# print(bin(b))