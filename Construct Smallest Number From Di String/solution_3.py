class Solution:
    def smallestNumber(self, pattern: str) -> str:
        generated_strings = set()
        available_numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        pat_len = len(pattern)

        def generate(current_string, current_index, left):
            if len(current_string) == pat_len + 1:
                generated_strings.add(current_string)
                return

            for n in sorted(left):
                if current_string:
                    if (pattern[current_index] == 'I' and n > current_string[-1]) or \
                       (pattern[current_index] == 'D' and n < current_string[-1]):
                        new_left = left.copy()
                        new_left.remove(n)
                        generate(current_string + n, current_index + 1, new_left)
                else:
                    new_left = left.copy()
                    new_left.remove(n)
                    generate(current_string + n, current_index, new_left)

        generate('', 0, available_numbers)

        return min(generated_strings)