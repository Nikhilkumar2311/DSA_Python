"""

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

"""


def isIsomorphic(s: str, t: str) -> bool:
    indexS = [0] * 200  # Stores index of characters in string s
    indexT = [0] * 200  # Stores index of characters in string t

    length = len(s)  # Get the length of both strings

    if length != len(t):  # If the lengths of the two strings are different, they can't be isomorphic
        return False

    for i in range(length):  # Iterate through each character of the strings
        # Check if the index of the current character in string s is different
        # from the index of the corresponding character in string t
        if indexS[ord(s[i])] != indexT[ord(t[i])]:
            return False  # If different, strings are not isomorphic

        indexS[ord(s[i])] = i + 1  # updating position of current character
        indexT[ord(t[i])] = i + 1

    return True  # If the loop completes without returning false, strings are isomorphic


s = "egg"
t = "add"
print(isIsomorphic(s,t))
