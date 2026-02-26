nums=[4,2,7,4,9,2,1]

seen = set()
printed = set()

for num in nums:
    if num in seen and num not in printed:
        print(num)
        printed.add(num)
    seen.add(num)