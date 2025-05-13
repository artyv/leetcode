class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        d_sup = set(supplies)
        missing = {}
        graph = {}
        res = []

        for i, r in enumerate(recipes):
            cnt = 0
            for item in ingredients[i]:
                if item not in d_sup:
                    cnt += 1
                if item not in graph:
                    graph[item] = []  
                graph[item].append(r)
            missing[r] = cnt
        
        q = deque()
        for r in recipes:
            if missing[r] == 0:
                q.append(r)

        while q:
            r = q.popleft()
            res.append(r)
            d_sup.add(r)

            if r in graph:
                for dependent_recipe in graph[r]:
                    missing[dependent_recipe] -= 1
                    if missing[dependent_recipe] == 0:
                        q.append(dependent_recipe)
        
        return res