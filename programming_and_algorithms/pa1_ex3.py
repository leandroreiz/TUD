# def fun(a, b):
#   return a * b

# a = fun(2, 3)
# b = fun("2", 3)

# print(a, b) # 6 222
# print(a + b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ---------------------------

# def fun(n, m):
#   return m - n

# # case 1
# a = fun(fun(1, 2), 3)
# # fun((1), 3) = 2

# # case 2
# b = fun(fun(1, 2), fun(3, fun(fun(4, fun(5, 6)), 7)))
# # fun(1, fun(3, fun(fun(4, 1), 7)))
# # fun(1, fun(3, fun(-3, 7)))
# # fun(1, fun(3, 10))
# # fun(1, 7) = 6

# # case 3
# c = fun(fun(1, 2), fun(3, fun(fun(4, fun(5, 6)), fun(7,8))))
# # fun(1, fun(3, fun(fun(4, 1), 1)))
# # fun(1, fun(3, fun(-3, 1)))
# # fun(1, fun(3, 4))
# # fun(1, 1) = 0

# print(a, b, c)
# # if the return was substituted by print the system would throw an error (TypeError: unsupported operand type(s) for -: 'int' and 'NoneType') due to the function being NoneType

# ---------------------------

# def alpha(x, y):
#   return x + beta(y, x)

# def beta(x, y):
#   # return y - x # [1]
#   return x - y

# print(alpha(2, 3))
# # 2 + beta(3, 2)
# # 2 + (-1) = 1
# # [1] 2 + 1 = 3

# ---------------------------

# a = [1, 2, 3, 4]
# print(a)       # prints [1, 2, 3, 4]

# a[1:2] = []
# print(a)       # prints [1, 3, 4]

# a[1] = []      # This will cause a TypeError

# ---------------------------

# num / 12 = 1
# 123 % 100 = 23
# 8 + 3 * 7 = 29
# (0 == 1) and (2 < 3) = false and true = false
# not ((4.5 < 12.9) and (6 * 2 <= 13)) = not (true and true) = false
# (0 == 1) or ( 2 < 3) = false or true = true
# (0 == 1) or (2 < 3) and (7 < 6) = false or (true and false) = false or true = false
# (2 < 3) or (0 == 1) and (7 < 6) = true or (false and false) = true or true = true

# ---------------------------

# d = {"apple": "a round fruit with red or green skin", "banana": "a long, yellow fruit", "orange": "a round acid fruit"}
# print(d) # {'apple': 'a round fruit with red or green skin', 'banana': 'a long, yellow fruit', 'orange': 'a round acid fruit'}

# del d["apple"]
# print(d) # {'banana': 'a long, yellow fruit', 'orange': 'a round acid fruit'}

# d_item = d.pop("orange")
# print(d_item) # a round acid fruit

# d.clear()
# print(d) # {}

# ---------------------------

class Palindrome:
  def reverse(self, s):
    return s[::-1]

  def isPalindrome(self, s):
    return s == self.reverse(s)

# Test
p = Palindrome()

test_strings = ['hello', 'peel', 'peep', 'deed', 'dad']

for s in test_strings:
  if p.isPalindrome(s):
    print(s, "is a palindrome.")
  else:
    print(s, "is not a palindrome.")