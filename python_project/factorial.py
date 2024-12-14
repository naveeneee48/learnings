# def factorial_value():
# def len_array(input_value):
#     return len(input_value)
# print(len_array(["naveen",2,0.5]))
# my_list = [1,2,3,4]
# # print(my_list[2])
# def print_elements(element):
#     for i in my_list:
        

# def largest(Input):
        
#     # largest = Input[0]

#     # for item in Input:
#     #     if item > largest:
#     #         print(item)
#     #         largest = item

    
#     # print(largest)
#     Input.sort()
#     # sorted(Input)
#     print(Input)
# largest([30, 40, 10, 20, 50])



# name = "naveen"
# name = "kumar"
# print(name)


def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))