class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = sorted(Counter(word).values(), reverse=True)
        order = 1; cnt = 0
        pushes = 0; n_buttons = 8

        for times in counter:
            cnt += 1
            pushes += order * times
            if cnt == n_buttons:
                cnt = 0
                order += 1
        return pushes

