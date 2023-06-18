from collections import deque

s = "abba"

q = deque()

q.append(['a', 1])
q.append(['b', 2])
q.append(['c', 3])
# for i in q:
#     print(i)

# q.popleft()
# print(q)

# for i in range(len(q)):
#     if q[i][0] == 'b':
#         print(q[i][1])

for i in range(len(q)):
    if q[i][0] == 'b':
        print("found")
        for j in range(0, i+1):
            q.popleft()
            j+=1
        break
    # else:
    #     print("no")
print(q)

# def longest_substring(s):
#     queue = deque()
#     for i in range(len(s)):
#         for j in queue:
#             if j[0]==s[i]:
                
#         else:
#             queue.append([s[i], i])