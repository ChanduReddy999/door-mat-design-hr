"""Designer door mat pattern using python (hackerrank)"""

'''method 1'''

# N, M = map(int, input().split())
# for i in range(1, N, 2):
#     print((i * ".|.").center(M,"-"))
# print("WELCOME".center(M, "-"))
# for i in range(N-2, -1, -2):
#     print((i * ".|.").center(M, "-"))

'''method 2'''

# N,M = map(int,input().split())
# #Upper Part
# for i in range(int(N/2)):
#     pattern = '.|.'*(i*2+1)
#     print(pattern.center(M, "-"))
# #Center
# print("WELCOME".center(M,"-"))
# #Lower
# for i in range(int(N/2),0,-1):
#     pattern = ".|."*(i*2-1)
#     print(pattern.center(M, "-"))

'''method 3'''

# N,M = map(int,input().split())
# Pattern = '.|.'
# for i in range(int(N/2)): print((Pattern*((i*2)+1)).center(M,'-'))
# print('WELCOME'.center(M,'-'))
# for i in range(int(N/2)-1,-1,-1): print((Pattern*((i*2)+1)).center(M,'-'))

'''method 4'''

# N, M = map(int,input().split())
# st='.|.'
# mid = int((N+1)/2)
# for i in range(1,mid+1):
#     if i != mid:
#         print(st.center(M,'-'))
#         st= st+'.|.'*2  
#     if i == mid:
#         print('WELCOME'.center(M,'-'))
# st = st.replace('.|.', '', 2)      
# for i in range(1,mid):
#     print(st.center(M,'-'))
#     st= st.replace('.|.', '', 2)

