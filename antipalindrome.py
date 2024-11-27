string = [ch.lower() for ch in input() if ch.isalpha()]

is_palindrome = False

for i in range(len(string) - 2):
    if string[i] == string[i+1] or string[i] == string[i+2]:
        is_palindrome = True
        break
if string[-2] == string[-1]:
    is_palindrome = True
    
print("Palindrome" if is_palindrome else "Anti-palindrome")
