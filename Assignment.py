def classify(value):
    if value<48:
        return "Below range"
    elif 48<=value<=52:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    average=total/count
    return average

cables=int(input("Enter the number of cables:"))

total_length=0
below=0
in_range=0
above=0

for _ in range(cables):
    length=int(input("Enter the cable length:"))
    classification=classify(length)
    print(classification)

    total_length+=length

    if classification=="Below range":
        below+=1
    elif classification=="In range":
        in_range+=1
    else:
        above+=1

average_length=calculate_average(total_length, cables)

print(f"Total length: {total_length} cm")
print(f"Average length: {average_length} cm")
print(f"Below range: {below}")
print(f"In range: {in_range}")
print(f"Above range: {above}")