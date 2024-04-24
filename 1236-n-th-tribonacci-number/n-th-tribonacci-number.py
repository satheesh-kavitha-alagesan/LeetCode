class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            qu = deque()
            qu.append(0)
            qu.append(1)
            qu.append(1)
            pointer = 3
            while pointer < n:
                qu.append(qu[0] + qu[1] + qu[2])
                qu.popleft()
                pointer +=1
            return qu[0] + qu[1] + qu[2]