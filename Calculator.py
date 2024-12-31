def cal(nums):
    try:
        print(eval(nums)),cal(input('Combination: '))
    except NameError:
        print('Only numbers'),cal(input('Combination: '))
    except SyntaxError:
        print('Only numbers'), cal(input('Combination: '))
cal(input('Combination: '))