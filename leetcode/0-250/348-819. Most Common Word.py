# 819. Most Common Word
import collections, re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punct = set('!?\',;.')
        clean_parag = []
        for c in paragraph.lower():
            if c not in punct: clean_parag.append(c)
            else: clean_parag.append(' ')
        clean_parag = ''.join(clean_parag).split()
        for word, cnt in sorted(collections.Counter(clean_parag).items(), key=lambda item: item[1], reverse=True):
            if word not in banned:
                return word

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in banned).most_common(1)[0][0]