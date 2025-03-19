class DisJointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weights = [1]*(n)

    def findUPar(self, ind):
        if self.parent[ind] != ind:
            self.parent[ind] = self.findUPar(self.parent[ind])  # Path compression
        return self.parent[ind]
    
    def unionBySize(self, u, v):
        rootU = self.findUPar(u)
        rootV = self.findUPar(v)

        if rootV==rootU:
            return 
        
        if self.weights[rootU] < self.weights[rootV]:
            self.parent[rootU] = self.parent[rootV]
            self.weights[rootV] += self.weights[rootU]

        else:
            self.parent[rootV] = self.parent[rootU]
            self.weights[rootU] += self.weights[rootV]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisJointSet(n)
        mpp = {}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in mpp:
                    mpp[accounts[i][j]] = i 
                else:
                    ds.unionBySize(i, mpp[accounts[i][j]])
        mergedMail = [[] for _ in range(n)]

        for u,v in mpp.items():
            node = ds.findUPar(v)
            mergedMail[node].append(u)

        ans = []
        
        # print(mergedMail)
        for i in range(n):
            if mergedMail[i]:
                tmp = sorted(mergedMail[i])
                print(tmp)
                ans.append([accounts[i][0]]+tmp)
        
        return ans


        # print(mpp)
        # print(ds.parent)
        # return [[]]