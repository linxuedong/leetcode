# 面试题 01.05. 一次编辑
# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

# 示例 1:
# 输入: 
# first = "pale"
# second = "ple"
# 输出: True

# 示例 2:
# 输入: 
# first = "pales"
# second = "pal"
# 输出: False

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/one-away-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def oneEditAway1(self, first: str, second: str) -> bool:
        l1 = len(first)
        l2 = len(second)
        if abs(l1 - l2) > 1: return False

        for i in range(min(l1, l2)):
            # 相等继续遍历
            if first[i] == second[i]:
                continue
                
            # 新增操作 或 删除操作
            if first[i+1:] == second[i:] or first[i:] == second[i+1:]:
                return True
            # 修改操作
            elif first[i+1:] == second[i+1:]:
                return True
            else:          
                return False
        return True


    def oneEditAway(self, first: str, second: str) -> bool:
        # 长度相差大于 1，则操作超过 1 次
        l1, l2 = len(first), len(second)
        if abs(l1 - l2) > 1: return False

        # 长度相等只有修改操作
        if l1 == l2:
            replace_count = 0
            for i in range(l1):
                if first[i] != second[i]:
                    replace_count += 1
                if replace_count > 1:
                    return False
            return True

        # 保持 first 比 second 长度长
        if l1 < l2: first, second = second, first

        for i in range(len(first)):
            # 删除操作
            if first[:i] + first[i+1:] == second:
                return True
        return False






if __name__ == "__main__":
    assert Solution().oneEditAway('','') == True
    assert Solution().oneEditAway('pale', 'ple') == True
    assert Solution().oneEditAway('pales', 'pal') == False
    assert Solution().oneEditAway('pales', 'palse') == False
    assert Solution().oneEditAway('pale', 'pala') == True

    
