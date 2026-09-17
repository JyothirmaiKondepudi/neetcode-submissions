class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trackerDict = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in trackerDict:
                trackerDict[s].append(i)
            else:
                trackerDict[s]=[i]
        
        return [v for v in trackerDict.values()]