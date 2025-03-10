"""
This is for my finance class lmaoooo.
"""


arr = []

ans_1 = 1000 * (1/(1.14)**20) + 105 * ((1 - (1/(1.4)**20))/.14)
arr.append({"q1": ans_1})

ans_2 = 1000 * (1/ (1.03)**20) + 57.5 * ((1 - (1/(1.03)** 20 ))/ .03)
arr.append({"q2": ans_2})

ans_3 = (.14 * 1000000 )/ 769420
arr.append({"q3": ans_3})

ans_4 = -35000 + (14000 / 1.12) + (14000 / 1.12 ** 2) + ( 14000 / 1.12 ** 3) + (14000 / 1.12 ** 4)
arr.append({"q4 proj y": ans_4})

ans_5 = -70000 + (27000 / 1.12) + (27000 / 1.12 ** 2) + (27000 / 1.12 ** 3) +(27000 / 1.12 ** 4)
arr.append({"ans 5 proj z": ans_5})

ans_6 = [35000 / 14000, 70000 / 27000]
arr.append({"ans 6": ans_6})


if __name__ == "__main__":
    for item in arr:
        print(item)
