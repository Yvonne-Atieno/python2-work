#Write a function that takes an unknown number of arguments and returns their sum.
def sum_args(*args):
    return sum(args)
print(sum_args(1, 2, 3))

#Write a function that takes two arguments, the first being a string and the second being an unknown number of integers. The function should return a new string where the integers have been added to the original string.
def add_integers_to_string(string, *integers):
    result = string
    for integer in integers:
        result += str(integer)
    return result
print(add_integers_to_string("The sum of ", 2, 3, 5, 6, 10, " is ", 20))
#Write a function that takes an unknown number of keyword arguments and returns a dictionary where the keys are the argument names and the values are the argument values.
def dict_from_kwargs(**kwargs):
    return kwargs
print(dict_from_kwargs(name='yvonne',age=32, country='Nairobi'))
#Write a function that takes a function and an unknown number of arguments, and returns the result of calling the function with the arguments.
def add_numbers(x, y):
    return x + y

print(call_function(add_numbers, 5, 7)) 

def multiply_numbers(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(call_function(multiply_numbers, 2, 3, 4, 5))
#Write a function that takes a list of integers and an unknown number of keyword arguments. The function should return a new list where each integer in the original list has been multiplied by the value of the corresponding keyword argument.
def multiply_list_by_kwargs(int_list, **kwargs):
    result = []
    for i, num in num(int_list):
        if i < len(kwargs):
            result.append(num * list(kwargs.values())[i])
        else:
            result.append(num)
    return result
print(multiply_list_by_kwargs([3, 5, 8, 11, 12], ))
#Write a function that takes a list of integers and an unknown number of additional integers as arguments. The function should return the index of the first occurrence of the sum of the list and the additional integers


#Write a function that takes an unknown number of keyword arguments, each with a string value. The function should concatenate all the strings and return the resulting string.
def concat_strings(**kwargs):
    return ''.join(kwargs.values())
print(concat_strings(a='Hello ', b='world')) 