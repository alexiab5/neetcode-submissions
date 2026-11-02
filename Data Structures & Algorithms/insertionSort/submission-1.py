# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        insertions = []
        for i in range(0, len(pairs)):
            j = i - 1
            current = pairs[i]
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                pairs[j + 1] = pairs[j]
                pairs[j] = current
                j -= 1
            insertions.append(pairs.copy())
        return insertions

        