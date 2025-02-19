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



if __name__ == "__main__":
    for item in arr:
        print(item)
