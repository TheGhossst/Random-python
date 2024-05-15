class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(reverse = True)
        print(f"people -> {people}")
        boats = 0
        start = 0 
        end = len(people) - 1

        while (start <= end):
            if people[start] + people[end] <= limit:
                print(f"{people[start]} + {people[end]} <= {limit}")
                start += 1
                end -= 1
            else:
                print(f"{people[start]} + {people[end]} > {limit}")
                start += 1
            boats += 1
            print(f"Boats -> {boats}")
        return boats

if __name__ == "__main__":
    people = [3,2,2,1]
    limit = 3
    solution = Solution()
    result = solution.numRescueBoats(people, limit)
    print(result)