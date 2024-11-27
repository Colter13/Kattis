alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_indices = {letter: index for index, letter in enumerate(alphabet)}

def find_shift_letter(encrypted_letter, decrypted_letter):
    shift_index = (letter_indices[encrypted_letter] - letter_indices[decrypted_letter]) % 26
    return alphabet[shift_index]

def find_shift_phrase(encrypted_phrase, decrypted_phrase):
    return ''.join(map(lambda x, y: find_shift_letter(x, y), encrypted_phrase, decrypted_phrase))

# Input
peeked_letters, total_letters = map(int, input().split())
peeked = input()
encrypted_text = list(input())

# Find Shift Key
shift_phrase = peeked
shift_key = ''
for i in range(total_letters // peeked_letters):
    shift_phrase = find_shift_phrase(encrypted_text[-peeked_letters*(i+1):], shift_phrase)
    shift_key = shift_phrase + shift_key
shift_phrase = find_shift_phrase(encrypted_text[:total_letters % peeked_letters], shift_phrase[peeked_letters - (total_letters % peeked_letters):])
shift_key = shift_phrase + shift_key

# Find Decrypted Message
decrypted_text = find_shift_phrase(encrypted_text, shift_key)
print(decrypted_text)
