class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = defaultdict(int)
        for num in nums:
            store[num] = store[num] + 1
            if store[num] == 3:
                del store[num]
        print(f'{store = }')
        return list(store.keys())[0]