f = open("numbers.txt", "r")

nums = [int(line.strip()) for line in f]

total = sum(nums)
avg = total / len(nums)

print("Total:", total)
print("Average:", avg)

f.close()
