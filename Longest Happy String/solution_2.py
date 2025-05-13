class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        smax = ''
        my_list = sorted([ [x[0], x[1]] for x in [['a', a], ['b', b], ['c', c]] if x[1] > 0], key=lambda x: x[1])

        last_letter = 'w'
        while len(my_list) > 1:
            i = -1 if my_list[-1][0] != last_letter else -2
            last_letter = my_list[i][0]

            temp = 2 if (my_list[i][1] >= 2 and i != -2) else 1
            smax += my_list[i][0] * temp
            if my_list[i][1] == temp:
                my_list.pop(i)
            else:
                my_list[i][1] -= temp
            my_list.sort(key=lambda x: x[1])
        
        if last_letter != my_list[-1][0]:
            temp = 2 if my_list[-1][1] >= 2 else 1
            smax += my_list[-1][0] * temp

        return smax