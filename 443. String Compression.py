class Solution:
    def compress(self, chars: List[str]) -> int:

        if not chars:
            return chars

        if len(chars) == 1:
            return 1
        else:
            index = 1
            while index < len(chars):
                count = 1
                while index < len(chars) and chars[index] == chars[index - 1]:
                    count += 1
                    chars.pop(index)
                temp = list(str(count))
                offset = len(temp)
                if count > 1:
                    for ele in temp:
                        chars.insert(index, ele)
                        index += 1
                    index += 1
                else:
                    index += 1
            return len(chars)

