from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)

        for str in strs:
            key = "".join(sorted(str))
            track[key].append(str)

        return list(track.values())
