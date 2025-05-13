class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_dict = {c:magazine.count(c) for c in magazine}
        for c in ransomNote:
            if magazine_dict.get(c, 0) == 0:
                return False
            else:
                magazine_dict[c] -= 1
        return True