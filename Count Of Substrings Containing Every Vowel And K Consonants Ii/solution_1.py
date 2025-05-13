class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._atLeastK(word, k) - self._atLeastK(word, k + 1)

    def _atLeastK(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l = len(word)
        counter = 0
        left = 0
        vowel_count = {}
        consonant_count = 0

        for right in range(l):
            char = word[right]

            if char in vowels:
                vowel_count[char] = vowel_count.get(char, 0) + 1
            else:
                consonant_count += 1

            # Подсчет подстрок с >= k согласными
            while len(vowel_count) == 5 and consonant_count >= k:
                counter += (l - right)
                left_char = word[left]
                if left_char in vowels:
                    vowel_count[left_char] -= 1
                    if vowel_count[left_char] == 0:
                        del vowel_count[left_char]
                else:
                    consonant_count -= 1
                left += 1

        return counter
