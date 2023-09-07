# Challenge 1

def sum_to(n):
    sum = 0
    for num in range(0, (n + 1)):
        sum += num
    return sum

    # tests for challenge 1

print('sum_to test one, sum_to(10) expected result: 55')
print(f'result: {sum_to(10)}')
print('sum_to test two, sum_to(5) expected result: 15')
print(f'result: {sum_to(5)}')

# Challenge 2

def largest(list):
    largest_num = 0
    for num in list:
        if num > largest_num:
            largest_num = num
    return largest_num

    # tests for challenge 2

print('largest test one, largest([10, 20, 35, 55, 6]) expected result: 55')
print(f'result: {largest([10, 20, 35, 55, 6])}')
print('largest test two, largest([5, 14, 3, 15, 1]) expected result: 15')
print(f'result: {largest([5, 14, 3, 15, 1])}')

# Challenge 3

def occurrences(str1, str2):
    str2_count = 0
    for idx in range(0, len(str1)):
        if str1[idx:(idx + len(str2))] == str2:
            str2_count += 1
    return str2_count

    # tests for challenge 3

print('occurrences test one, occurrences("geordie greep", "e") expected result: 4')
print(f'result: {occurrences("geordie greep", "e")}')
print('occurrences test two, occurrences("cavalcade", "ca") expected result: 2')
print(f'result: {occurrences("cavalcade", "ca")}')

# Challenge 4

def product(*args):
    res = 1
    for num in args:
        res *= num
    return res

    # tests for challenge 4

print('product test one, product(-1, 4) expected result: -4')
print(f'result: {product(-1, 4)}')
print('product test two, product(2, 5, 5) expected result: 50')
print(f'result: {product(2, 5, 5)}')

# Bonus Challenge


def steps_to_zero(int):
    steps = 0
    while int != 0:
        if int % 2 == 0:
            int /= 2
            steps += 1
        else:
            int -= 1
            steps += 1
    return steps


    # tests for bonus challenge


print('steps_to_zero test one, steps_to_zero(14) expected result: 6')
print(f'result: {steps_to_zero(14)}')
print('steps_to_zero test two, steps_to_zero(10) expected result: 5')
print(f'result: {steps_to_zero(10)}')





# def inner_changer(int):
#     the_num = int
#     def the_changer_itself():
#         nonlocal the_num
#         the_num += 2
#     the_changer_itself()
#     return the_num


# print(f'7 + 2 should be 9, however inner_changer yields {inner_changer(7)}')


# overlong and soulcrushing version of bonus challenge:


# def steps_to_zero(int):
#     # declare result variable with an initial value of zero
#     step_res = 0.0
#     def step_recur(num, step):
#         # check if num is not zero and divisible by two
#         if num != 0 and num % 2 == 0:
#             # divide num by two and store in new_num
#             new_num = num / 2
#             # increase the step count by one
#             step += 1
#             # log out details of this step
#             print(f'Step {step}) {num} is even, divide by 2 and obtain {new_num}')
#             # call recursive function again, passing the newly divided num and current step count as arguments
#             step_recur(new_num, step)
#         # check if num is not zero, no need to make sure it isn't divisble by two as it would have passed the previous conditional
#         elif num != 0:
#             # subtract 1 from num and store in new_num
#             new_num = num - 1
#             # increase step count
#             step += 1
#             # log out details of this step
#             print(f'Step {step}) {num} is odd, subtract by 1 and obtain {new_num}')
#             # call recursive function again, passing newly subtracted num and current step as arguments
#             step_recur(new_num, step)
#         # should num be equal to zero set result to current step count, as there is no need to iterate further
#         else: 
#             # set res to be equal to the current step count
#             nonlocal step_res
#             step_res = step
#             # log what res is set to
#             print(f'the recursive function is complete, res is now {step_res}')
#     # call step_recur passing the integer initially passed as the starting num, with the initial step count being 0
#     step_recur(int, 0)
#     # return (what should be) the resultant step count
#     return step_res

