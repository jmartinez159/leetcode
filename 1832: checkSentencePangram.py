class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphaStr = 'abcdefghijklmnopqrstuvwxyz'
        valid = {}
        for ch in sentence:
            valid[ch] = valid.get(ch, 0)+1
        for ch in alphaStr:
            cur = valid.get(ch, 0)
            if cur < 1:
                return False
        return True