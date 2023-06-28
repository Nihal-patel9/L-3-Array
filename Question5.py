def plusOne(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
            break

    if carry == 1:
        digits.insert(0, carry)

    return digits


digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]
