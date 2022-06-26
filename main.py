class Converting(object):
    def __init__(self):
        self.dict_of_letters = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        self.result = 0

    def roman_to_int(self, s):
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                self.result += self.dict_of_letters[s[i]]
                i += 1
            elif self.dict_of_letters[s[i]] < self.dict_of_letters[s[i+1]]:
                self.result -= self.dict_of_letters[s[i]]
                self.result += self.dict_of_letters[s[i+1]]
                i += 2
            else:
                self.result += self.dict_of_letters[s[i]]
                i += 1

        return self.result


if __name__ == '__main__':
    input_s = input()
    a = Converting()
    print(a.roman_to_int(input_s))
