# count upper and lower

def count_char(text):
    count_upper = 0
    count_lower = 0
    for i in text:
        if i.isalpha():
            if i.isupper():
                count_upper += 1
            elif i.lower():
                count_lower += 1
    return count_upper, count_lower

if __name__ == '__main__':
    text = input()

    count_upper, count_lower = count_char(text)

    print(f"Number of upper case in '{text}' is {count_upper}")
    print(f"Number of lower case in '{text}' is {count_lower}")