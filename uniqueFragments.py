# Given a string `s` of length `n` and number `k` where `n/k=0`,
     #divide the string into k fragments such that all characters in the given all fragments are unique.
def generate_substr(s, k):
    if not s or k == 0:
        return None
    
    result = {}

    for i in range(len(s)):
        if len(s)-i <k:
            break
        if len(set(s[i:i+k]))==k:
            result[s[i:i + k]] = 1
    return result.keys()

print(generate_substr('aabdddddcghssas',3))

#outpu:
# dict_keys(['abd', 'dcg', 'cgh', 'ghs'])