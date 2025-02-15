# from itertools import combinations

# def solution(numbers):
#     count = 0
#     trios = list(combinations(numbers, 3))

#     for trio in trios:
#         if sum(trio) == 0:
#             count += 1

#     return count
    
#     # count = 0

#     # for i in numbers[:]:
#     #     # print(numbers[:])
#     #     for j in numbers[1:]:
#     #         # print(numbers[1:])
#     #         for k in numbers[2:]:                
#     #             # print(numbers[2:])
#     #             if i + j + k == 0:
#     #                 print(i, j, k)
#     #                 count += 1 

#     # return count


# print(solution([-1, 1, -1, 1]))
# print(solution([-2, 3, 0, 2, -5]))
# print(solution([-3, -2, -1, 0, 1, 2, 3]))

'''
1. 학생마다 같은 값을 가질 순 있다.
2. 한 학생이 2번 이상 나올 순 없다.
3. 조합이 중복되선 안된다. 예) (학생1, 학생2, 학생3), (학생2, 학생1, 학생3), (학생3, 학생2, 학생1), ...

'''
 
