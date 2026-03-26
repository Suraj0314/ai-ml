numbers = []

while True:
    num = input("Enter number or done: ")
    
    try:
        if num.lower() == "done":
            break
        else:
            numbers.append(int(num))    
    except ValueError:
        print("Invalid input! Try again.")

if len(numbers) == 0:
    print("No numbers entered.")
    exit()

total = sum(numbers)
avg = total / len(numbers)

print(f"Largest: {max(numbers)}")
print(f"Smallest: {min(numbers)}")
print(f"Sum: {total}")
print(f"Average: {avg}")

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")