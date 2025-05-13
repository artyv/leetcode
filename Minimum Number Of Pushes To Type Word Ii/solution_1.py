class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = sorted(Counter(word).items(), key=lambda x: x[1], reverse=True)
        cnt = 0
        pushes = 0; n_buttons = 8

        for key, times in counter:
            cnt += 1
            pushes += (cnt // (n_buttons+1) + 1) * times
        return pushes

