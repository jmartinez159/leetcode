class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        products = {}
        i = 0
        for x in arr:
            curr = x*2
            if products.get(curr) == None:
                products[curr] = []
            products[curr].append(i)
            i+=1
        
        for i in range(len(arr)):
            if products.get(arr[i]) is None:
                continue
            else:
                for x in products[arr[i]]:
                    if x != i:
                        return True
        return False