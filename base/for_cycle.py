# data = [1, 2, 3, 4]
# for i in data:
#     print(i)
# else:
#     print("end")

data = [["1", 2, 3, 4], ["a", "b", "c", True]]

# for i in data[0]:
#     print(i)

for x in data:
    print(x)
    for j in x:
        print(j)
        if j == "1":
            break
        print(j)

else:
    print("end")

print("for++")
data = [1, 2, 3, 4, 5]
for x in range(0, 10):
    print(x)

for x in range(0,10,2):
    print(x,end="|")