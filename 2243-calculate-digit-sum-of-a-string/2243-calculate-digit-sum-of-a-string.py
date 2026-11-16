class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            arr = []
            string = ""

            # Divide s into groups of size k
            for i in range(0, len(s), k):
                arr.append(s[i:i+k])

            # Calculate sum of each group
            for a in arr:
                total = 0

                for b in a:
                    total += int(b)

                string = string + str(total)

            # Update s for next round
            s = string

        return s