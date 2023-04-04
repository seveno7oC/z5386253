workinghours = int(input("How long do you work every week?"))
if workinghours <= 35:
    print("The rate is 54.45 per hour")
elif workinghours > 35:
    print("The rate is 88.9 per hour")

#example
hours = input('Enter your working hours this week')
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9

if hours > 35:
    pay= (35 * normal_rate)+((hours - 35)*overload_rate)
else:
    pay= hours * normal_rate

print(f'This weekly payment is : {pay}')
