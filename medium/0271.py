""" Encode And Decode Strings """
# O(n)
class Codec:
    def encode(self, strs):
        o = ""
        for s in strs:
            o += str(len(s)) + "#" + s
        return o

    def decode(self, s):
        print(s)
        o, i, t = [], 0, ""
        while i < len(s):
            c = s[i]
            if c == '#':
                n = i + int(t) + 1
                o.append(s[i + 1:n])
                i = n
                t = ""
            else:
                t += c
                i += 1
        return o