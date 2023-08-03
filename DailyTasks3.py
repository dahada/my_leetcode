class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dialing = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}

        if not digits:
            return []

        def rec_func(combination, next_digits):
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for elem in dialing[next_digits[0]]:
                    rec_func(combination + elem, next_digits[1:])

        res = []
        rec_func('', digits)

        return res