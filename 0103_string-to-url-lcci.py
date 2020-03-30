class Solution:
    def replaceSpaces1(self, S: str, length: int) -> str:
        result = S[:length].split(' ')
        return '%20'.join(result)


    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(' ', '%20')


if __name__ == "__main__":
    assert Solution().replaceSpaces("Mr John Smith    ", 13) == "Mr%20John%20Smith"
    assert Solution().replaceSpaces("               ", 5) == "%20%20%20%20%20"
