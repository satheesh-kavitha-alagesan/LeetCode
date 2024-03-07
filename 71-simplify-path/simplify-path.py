class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip('/').split('/')
        stack = []
        for p in path:
            if p in ('.', ''):
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        ret = '/'.join(stack)
        return ret if ret.startswith('/') else '/'+ret