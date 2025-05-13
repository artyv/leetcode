class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        d = dict()
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        print(f"{len(nums)=}")
        print(f"{d=}")
        distance = dict()
        aux = list(d.keys())
        l = len(aux)
        for i in range(l):
            n = d[aux[i]]
            if 0 in distance:
                distance[0] += n*(n-1)//2
            else:
                distance[0] = n*(n-1)//2
            for j in range(i+1, l):
                m = d[aux[j]]
                if abs(aux[i]-aux[j]) in distance:
                    distance[abs(aux[i]-aux[j])] += m*n
                else:
                    distance[abs(aux[i]-aux[j])] = m*n

        for key in sorted(distance.keys()):
            k -= distance[key]
            if k <= 0:
                return key