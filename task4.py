def PalindromeFilter(arg, minLength):
    def palindrome_strings(arg, minLength):
        result = []
        for string in arg:
            if string == string[::-1] and len(string) >= minLength:
                result.append(string)
        return result

