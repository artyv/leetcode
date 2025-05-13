class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive_heaps_algorithm(perms, l): #l = len(perms)
            if l == 1:
                yield perms
            else:
                for perm in map(list, recursive_heaps_algorithm(perms, l-1)):
                    yield perm
                for i in range(l-1):
                    if l % 2 == 0:
                        perms[i], perms[l-1] = perms[l-1], perms[i]
                    else:
                        perms[0], perms[l-1] = perms[l-1], perms[0]
                    for perm in map(list, recursive_heaps_algorithm(perms, l-1)):
                        yield perm
        return(list(recursive_heaps_algorithm(nums, len(nums))))

