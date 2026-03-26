numbers = []
for i in range(5):
    user = int(input("Enter number: "))
    numbers.append(user)
print(f"Largest: {max(numbers)}")
print(f"Smallest: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")

even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    if i % 2 != 0:
        odd += 1 
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")           