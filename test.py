# # Brute Force - 2965: Find Missing and Repeated Values
# # class Solution(object):
# #     def count(self, lst, i):
# #         counter=0
# #         for j in lst:
# #             if j==i:
# #                 counter+=1
# #         return counter
                
        
# #     def findMissingAndRepeatedValues(self, grid):
# #         """
# #         :type grid: List[List[int]]
# #         :rtype: List[int]
# #         """
# #         flatten_grid = [i for j in grid for i in j]
# #         flatten_grid_dic = {i:self.count(flatten_grid,i) for i in flatten_grid}
# #         print(flatten_grid)
# #         print(flatten_grid_dic)
# #         result = []
# #         repeated = []
# #         not_in_list = []
# #         for i in [j for j in range(1,len(grid)**2+1)]:
# #             if i not in flatten_grid_dic.keys():
# #                 not_in_list.append(i)
# #             elif flatten_grid_dic[i] > 1:
# #                 repeated.append(i)
# #         result = [i for i in repeated]
# #         for j in not_in_list:
# #             result.append(j)
# #         return result
        
# # print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))

# # Brute Force - 136: Single Number
# class Solution(object):
#     def count(self, lst, i):
#         counter=0
#         for j in lst:
#             if j==i:
#                 counter+=1
#         return counter
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         for num in nums:
#             counter = self.count(nums, num)
#             if counter == 1:
#                 return num

grid = [[2,1],[2,1],[2,1]]
for i in range(len(grid)):
    if i%2!=0:
        grid[i].reverse()
l = [i for j in grid for i in j]
ans = [l[i] for i in range(0,len(l),2)]
print(ans)