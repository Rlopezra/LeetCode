"""
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

 

Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
Example 3:

Input: n = 7
Output: "holasss"


*Note: My code is more memory intensive from commmon solutions since I opted to generate random strings instead of solely using the letters 'a' and 'b'
"""

class Solution:
    import random
    def generateTheString(self, n: int) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        if n%2 != 0:
            return random.choice(letters)*n
        else:
            return (random.choice(letters)*(n-1)+random.choice(letters))
