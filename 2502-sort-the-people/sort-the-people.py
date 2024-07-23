class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [i[0] for i in sorted([(nm, he) for nm, he in zip(names, heights)], key = lambda x: (-x[1], x[0]))]