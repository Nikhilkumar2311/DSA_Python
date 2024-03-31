# Finding len of No. of distinct substring from a given string
s = "abc"
sub = {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)}
print("No. of Substrings: ", len(sub))

# for printing SubString itself
print(sub)

# Or
s = "abc"
sub = set()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub.add(s[i:j])

print("No. of Substrings: ", len(sub))
