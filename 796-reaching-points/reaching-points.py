# class Solution:
#     def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
#         @cache
#         def solve(x,y):
#             if x>tx or y>ty: return False
#             if x==tx and y==ty: return True

#             return solve(x+y,y) or solve(x,y+x)

#         return solve(sx,sy)

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:

            if tx == ty:
                break

            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0

            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy