# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         ret = []
#         if len(nums) < 4:
#             return ret
#         nums.sort()
#         start = 0 
#         end = len(nums) -1
#         rotation = [(1,0), (-1,-1), (1,0)]
#         while start < end:
#             p1 = start+1
#             p2 = end -1
#             twopointtarget = target - (nums[start] + nums[end])
#             while p1 < p2:
#                 print(f'{p1 =}, {p2 = }, {twopointtarget = }, {nums[start] = }, {nums[end] = }, {nums[p1] = }, {nums[p2] = }')
#                 if nums[p1] + nums[p2] == twopointtarget:
#                     ret.append([nums[start], nums[p1], nums[p2], nums [end]])
#                     p1 +=1
#                     p2 -=1
#                 elif twopointtarget > p1 and twopointtarget <= p2:
#                     p1+=1
#                 elif twopointtarget < p2 and twopointtarget >= p1:
#                     p2-=1
#                 else:
#                     break
#             out = rotation.pop(0)
#             rotation.append(out)
#             startchange, endchange = out
#             start += startchange
#             end += endchange
#         return ret

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         n = len(nums)
#         seen = set()
#         ans = set()
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     lastNumber = target - nums[i] - nums[j] - nums[k]
#                     if lastNumber in seen:
#                         arr = sorted([nums[i], nums[j], nums[k], lastNumber])
#                         ans.add((arr[0], arr[1], arr[2], arr[3]))
#             seen.add(nums[i])
#         return ans

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         sortedElementList = sorted(nums)
#         result = []
#         self.nSumRecursive(sortedElementList, target, 4, result, [])
#         return result
        
#     def twoSum (self, listOfElements: list[int], target: int, resultList: list[list[int]], auxiliaryList: list[int], left: int) -> list[list[int]]:
#         sortedList = sorted(listOfElements)
#         lenght = len(sortedList)
#         right = lenght - 1
#         while (left < right):
#             if (sortedList[left] + sortedList[right] < target): 
#                 left+=1
#             elif (sortedList[left] + sortedList[right] > target):
#                 right -= 1
#             else:
#                 resultList.append(auxiliaryList + [sortedList[left], sortedList[right]])
#                 left+=1
#                 while(left < right and sortedList[left] == sortedList[left - 1]): left += 1

#         return

#     def nSumRecursive (self, listOfElements: list[int], target: int, nSum: int, resultList: list[list[int]], auxiliaryList: list[int], left: int = 0) -> list[list[int]]:
#         if (nSum == 2):
#             self.twoSum(listOfElements, target, resultList, auxiliaryList, left)
#         else:
#             indexLimit = len(listOfElements) - nSum + 1
#             for index in range(left, indexLimit):
#                 if (index == left or (listOfElements[index] != listOfElements[index - 1])):
#                     self.nSumRecursive(listOfElements, target - listOfElements[index], nSum - 1, resultList, auxiliaryList + [listOfElements[index]], index + 1)
#         return

class Solution:
    def fourSum(self, A, T):
        n = len(A)
        d = defaultdict(set)
        ans = set()
        for i in range(n):
            for j in range(i + 1, n):
                currentSum = A[i] + A[j]
                for pair in d[T - currentSum]:
                    ans.add(tuple(sorted((A[i], A[j]) + pair)))
            for k in range(i):
                currentSum = A[k] + A[i]
                d[currentSum].add((A[k], A[i]))
        print(ans)
        return ans
        