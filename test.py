s = input("Enter a sentence: ").strip().upper()
for x in "AEIOU":
    print(f"The frequency of '{x}' = {s.count(x)}")
