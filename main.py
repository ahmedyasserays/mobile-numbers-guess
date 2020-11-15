import random
first_nums = input("type the first_nums of the number: ")
temp_list = []
start = int(first_nums + ((11 - len(first_nums)) * "0"))
end = int(str(int(first_nums) + 1) + ((11 - len(first_nums)) * "0"))
file = open("valid numbers.txt", "a")
for i in range(start, end):
    temp_list.append("0" + str(i) + ":" + "0" + str(i) + "\n")

random.shuffle(temp_list)
file.writelines(temp_list)
file.close()
