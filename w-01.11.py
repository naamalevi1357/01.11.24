# start

# 2:
# a:
students: int = 103
class_students: int = 30
print(students // class_students)
print(students % class_students)

students_input: int = int(input("what is students ?"))
print(students_input // class_students)
print(students_input % 30)

# b:
number: int = 0
while True:
    try:
        number = int(input(" what is number ?"))
        if not 10 <= number <= 99:
            continue
        break
    except ValueError:
        print("Error str")

achadot = number % 10
asarot = number // 10
if achadot > asarot:
    sum_number = achadot * 10 + asarot
    print(sum_number)
else:
    print(number)

# c:
numbers: list[int] = []
for i in range(1, 200 + 1):
    if i < 2:
        continue
    if i == 2:
        numbers.append(i)
    if i % 2 == 0:
        continue
    divider = 2
    while divider < i:
        if i % divider == 0:
            break
        divider += 1
    else:
        numbers.append(i)
print(numbers)

# d:
mena_a: int = 0
mena_b: int = 0
mena_c: int = 0
mena_d: int = 0
answer: str = ""
answer_a_b_c_d: str = "abcd"
while True:
    answer: str = str(input(" what is answer ?"))
    if answer == "x":
        break
    if not answer in answer_a_b_c_d:
        continue
    match answer:
        case "a":
            mena_a += 1
        case "b":
            mena_b += 1
        case "c":
            mena_c += 1
        case "d":
            mena_d += 1
print(f"answer a {mena_a} ")
print(f"answer b {mena_b} ")
print(f"answer c {mena_c} ")
print(f"answer d {mena_d} ")

meneim:list[int]=[]
meneim.append(mena_a)
meneim.append(mena_b)
meneim.append(mena_c)
meneim.append(mena_d)
print(meneim)
index_max=meneim.index(max(meneim))
index_min=meneim.index(min(meneim))
print(index_min)
print(index_max)
print(answer_a_b_c_d[index_max])
print(answer_a_b_c_d[index_min])



# if mena_a > mena_b and mena_a> mena_c and mena_a>mena_d :
#     print(f"answer a big {mena_a}")
# elif mena_b > mena_a and mena_b > mena_c and mena_b > mena_d:
#     print(f"answer b big {mena_b}")
# elif mena_c > mena_a and mena_c > mena_b and mena_c > mena_d:
#     print(f"answer c big {mena_c}")
# elif mena_d > mena_a and mena_d > mena_b and mena_d > mena_c:
#     print(f"answer d big {mena_d}")
#
# if mena_a < mena_b and mena_a< mena_c and mena_a<mena_d :
#     print(f"answer a small {mena_a}")
# elif mena_b < mena_a and mena_b < mena_c and mena_b < mena_d:
#     print(f"answer b small {mena_b}")
# elif mena_c < mena_a and mena_c < mena_b and mena_c < mena_d:
#     print(f"answer c small {mena_c}")
# elif mena_d < mena_a and mena_d < mena_b and mena_d < mena_c:
#     print(f"answer d small {mena_d}")








# stop
