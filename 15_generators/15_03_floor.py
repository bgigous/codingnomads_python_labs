'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
def floor_by_1111(num_list):
    for n in num_list:
        yield n // 1111


for divisible in floor_by_1111([111, 1001, 1111, 2222, 2232, 5553, 12221]):
    print(divisible)
