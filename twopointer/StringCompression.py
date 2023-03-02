class Solution:
    def compress(self, chars: List[str]) -> int:

        def replace(i, chars, curr, cnt):
            chars[i] = curr
            i += 1
            if cnt > 1:
                start = i
                while cnt > 0:
                    chars[i] = str(cnt % 10)
                    i += 1
                    cnt = cnt // 10
                end = i - 1
                while start < end:
                    chars[start], chars[end] = chars[end], chars[start]
                    start += 1
                    end -= 1
            return i

        slow = cnt = 0
        ans = 0
        for fast in range(len(chars)):
            if chars[fast] == chars[slow]:
                cnt += 1
            else:
                ans = replace(ans, chars, chars[slow], cnt)
                slow, cnt = fast, 1
        ans = replace(ans, chars, chars[slow], cnt)
        return ans
