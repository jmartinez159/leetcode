class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # [ 3  3  4  5 ] res = 3
        #   ^i ^j

        people.sort()
        res = 0
        i, j = 0, len(people)-1
        while i <= j:
            if i == j:
                res +=1
                break
            elif (people[i]+people[j]) <= limit:
                i+=1
                j-=1
            else:
                j-=1
            res +=1
        
        return res