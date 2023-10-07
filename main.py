class Solution:
    def kdsWithCandiesi(self, candiess, extraCandies):
        max_candies = max(candiess)

        result = []
        for i in range(len(candiess)):
            if candiess[i] + extraCandies >= max_candies:  # Note the change here
                result.append(True)
            else:
                result.append(False)
        return result


candy = Solution()
candies = [5, 6, 7, 8]
extracandies = 9
result = candy.kidsWithCandies(candies, extracandies)
print(result)



