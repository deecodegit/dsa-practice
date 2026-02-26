def longest_substring_without_repeating_characters(s: str) -> int:
    char_map = set()  
    start = max_length = 0    
        
    for end in range(len(s)):
        while s[end] in char_map:
            char_map.remove(s[start])
            start += 1
            
        char_map.add(s[end])
        max_length = max(max_length, end - start + 1)
            
    return max_length

print(longest_substring_without_repeating_characters('abcdeefghijkk'))
print(longest_substring_without_repeating_characters(" "))
print(longest_substring_without_repeating_characters("abba"))