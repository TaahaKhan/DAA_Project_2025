import random
import re
import os

# --------------------------------------
# Helper Functions
# --------------------------------------

def findSum(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    for i in range(n2 - 1, -1, -1):
        sum_val = int(str1[i]) + int(str2[i]) + carry
        result = str(sum_val % 10) + result
        carry = sum_val // 10

    if carry:
        result = str(carry) + result

    return result

def findDiff(str1, str2):
    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    for i in range(n2 - 1, -1, -1):
        sub = int(str1[i]) - int(str2[i]) - carry
        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0
        result = str(sub) + result

    return result.lstrip('0') or "0"

def removeLeadingZeros(s):
    return re.sub("^0+(?!$)", "", s)

# --------------------------------------
# Karatsuba Multiplication (Strings)
# --------------------------------------

def multiply(A, B):
    A, B = removeLeadingZeros(A), removeLeadingZeros(B)
    if len(A) < 10 and len(B) < 10:
        return str(int(A) * int(B))

    n = max(len(A), len(B))
    n2 = n // 2
    A = A.zfill(n)
    B = B.zfill(n)

    Al, Ar = A[:n2], A[n2:]
    Bl, Br = B[:n2], B[n2:]

    p = multiply(Al, Bl)
    q = multiply(Ar, Br)
    r = multiply(findSum(Al, Ar), findSum(Bl, Br))
    r = findDiff(r, findSum(p, q))

    return removeLeadingZeros(findSum(findSum(p + '0' * (2 * (n - n2)), r + '0' * (n - n2)), q))

# --------------------------------------
# Generate Random Inputs (100–150 digits)
# --------------------------------------

os.makedirs("karatsuba_string_inputs", exist_ok=True)
os.makedirs("karatsuba_string_results", exist_ok=True)

def random_big_int(num_digits):
    # ensure no leading zero
    first = str(random.randint(1, 9))
    rest = ''.join(str(random.randint(0, 9)) for _ in range(num_digits - 1))
    return first + rest

for i in range(1, 11):
    digits = random.randint(100, 150)
    a = random_big_int(digits)
    b = random_big_int(digits)
    with open(f"karatsuba_string_inputs/input_{i}.txt", "w") as f:
        f.write(f"{a}\n{b}\n")

print("✅ Generated 10 input files (100–150 digit integers) in 'karatsuba_string_inputs/'")

# --------------------------------------
# Apply Karatsuba Multiplication on All Datasets
# --------------------------------------

for i in range(1, 11):
    with open(f"karatsuba_string_inputs/input_{i}.txt") as f:
        A, B = [line.strip() for line in f.readlines()]
        product = multiply(A, B)
        print(f"Dataset {i}: Product starts with {product[:60]}...")

    with open(f"karatsuba_string_results/result_{i}.txt", "w") as out:
        out.write(f"Product for dataset {i}:\n{product}\n")

print("✅ All results saved in 'karatsuba_string_results/'")