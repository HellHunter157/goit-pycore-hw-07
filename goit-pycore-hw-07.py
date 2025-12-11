





#перше завдання
# class HashTable:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def hash(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         index = self.hash(key)
#         for i, (k, v) in enumerate(self.table[index]):
#             if k == key:
#                 self.table[index][i] = (key, value)
#                 return
#         self.table[index].append((key, value))

#     def get(self, key):
#         index = self.hash(key)
#         for k, v in self.table[index]:
#             if k == key:
#                 return v
#         return None

#  
#     def delete(self, key):
#         index = self.hash(key)
#         bucket = self.table[index]
#         for i, (k, v) in enumerate(bucket):
#             if k == key:
#                 del bucket[i]
#                 return True
#         return False







#друге завдання


# def binary_search_with_upper_bound(arr, target):
#     left, right = 0, len(arr) - 1
#     iterations = 0
#     upper_bound = None

#     while left <= right:
#         iterations += 1
#         mid = (left + right) // 2
#         mid_val = arr[mid]

#         if mid_val >= target:
#             upper_bound = mid_val
#             right = mid - 1
#         else:
#             left = mid + 1

#     return (iterations, upper_bound)





#третє завдання








# import timeit


# def kmp_search(text, pattern):
#     def build_lps(pattern):
#         lps = [0] * len(pattern)
#         j = 0
#         for i in range(1, len(pattern)):
#             while j > 0 and pattern[i] != pattern[j]:
#                 j = lps[j - 1]
#             if pattern[i] == pattern[j]:
#                 j += 1
#             lps[i] = j
#         return lps

#     lps = build_lps(pattern)
#     i = j = 0
#     while i < len(text):
#         if text[i] == pattern[j]:
#             i += 1
#             j += 1
#             if j == len(pattern):
#                 return i - j
#         else:
#             if j > 0:
#                 j = lps[j - 1]
#             else:
#                 i += 1
#     return -1

# def boyer_moore(text, pattern):
#     m, n = len(pattern), len(text)
#     if m > n:
#         return -1

#     skip = {pattern[i]: m - i - 1 for i in range(m - 1)}

#     i = m - 1
#     while i < n:
#         k = 0
#         while k < m and pattern[m - 1 - k] == text[i - k]:
#             k += 1
#         if k == m:
#             return i - m + 1
#         i += skip.get(text[i], m)
#     return -1

# def rabin_karp(text, pattern):
#     m, n = len(pattern), len(text)
#     p_hash = hash(pattern)
#     for i in range(n - m + 1):
#         if hash(text[i:i+m]) == p_hash:
#             if text[i:i+m] == pattern:
#                 return i
#     return -1



# def measure(func, text, pattern):
#     return timeit.timeit(lambda: func(text, pattern), number=1000)

# text1 = open("article1.txt", encoding="utf-8").read()
# text2 = open("article2.txt", encoding="utf-8").read()

# pattern_exists = "the"     
# pattern_fake = "zzxqwr"    

# algorithms = [
#     ("Boyer-Moore", boyer_moore),
#     ("KMP", kmp_search),
#     ("Rabin-Karp", rabin_karp)
# ]

# for name, func in algorithms:
#     print("\n---", name, "---")
#     print("Text 1 / exists:", measure(func, text1, pattern_exists))
#     print("Text 1 / fake:",   measure(func, text1, pattern_fake))
#     print("Text 2 / exists:", measure(func, text2, pattern_exists))
#     print("Text 2 / fake:",   measure(func, text2, pattern_fake))
