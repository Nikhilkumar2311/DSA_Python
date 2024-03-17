# Finding len of No. of distinct substring from a given string
s = "abc"
sub = {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)}
print(len(sub))

# for printing SubString itself
print(sub)
