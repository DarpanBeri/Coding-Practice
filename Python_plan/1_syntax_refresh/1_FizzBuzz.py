"""
May 28, 2025.

Leetcode link: https://leetcode.com/problems/fizz-buzz/description/
412. Fizz Buzz.

Good Old FizzBuzz!
"""

"""
Basic Implementation.

Logic: Iterate over all the elements, do 3 checks for "FizzBuzz", "Fizz", and "Buzz" each.
Time complexity: O(n)
Space complexity: O(n)
"""

result = []
for elem in range(1, n+1):
    if elem % 3 == 0 and elem % 5 == 0:
        result.append("FizzBuzz")
    elif elem % 5 == 0:
        result.append("Buzz")
    elif elem % 3 == 0:
        result.append("Fizz")
    else:
        result.append(str(elem)) # The array being returned has to be a string array.

return result

"""
Implementation using Hashing.

Logic: reduces the number of modulo operation being done by concating fizz and buzz if % 3 or 5.
Time complexity: O(n)
Space complexity: O(n)
"""

result = []
for number in range(1, n+1):
    element = ""
    if number % 3 == 0:
        element = element + "Fizz"
    if number % 5 == 0:
        element += "Buzz"

    if len(element) > 0:
        result.append(element)
    else:
        result.append(str(number))

return result

"""
Implementation using Hashing / python's dict.

Logic: scalable to any possible replacables like "Jazz" for % 7 == 0.
Time complexity: O(n)
Space complexity: O(n)
"""

result = []
hash = {3: "Fizz",
        5: "Buzz"}

for number in range(1, n+1):
    element = ""
    for key in hash:
        if number % key == 0:
            element += hash[key]

    if not element: # i.e. if element be empty:
        element += str(number)

    result.append(element)

return result


"""
And thus the boss monster known as FizzBuzz was slayed for good and thousands of comp sci students sighed in relief.
"""
