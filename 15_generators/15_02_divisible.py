'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
def div_by_1111(num_list):
    for n in num_list:
        if n % 1111 == 0:
            yield n


for divisible in div_by_1111([111, 1001, 1111, 2222, 2232, 5553, 12221]):
    print(divisible)
