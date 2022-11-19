# This is a script that converts text to morse code

text = [a for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!"]
morse = [c for c in '.-c-...c-.-.c-..c.c..-.c--.c....c..c.---c-.-c.-..c--c-.c---c.--.c--.-c.-.c...c-c..-c...-c.--c-' \
                    '..-c-.--c--..c-----c.----c..---c...--c....-c.....c-....c--...c---..c----.c.-.-.-c--..--c..--..c-' \
                    '.-.--'.split('c')]

morse_dict = {key: value for key, value in zip(text, morse)}

inp = input("Enter your text: ").upper()
print("Morse code:", end=" ")
for ch in inp:
    try:
        print(morse_dict[ch], end=" ")
    except KeyError:
        if ch == " ":
            print(" ", end=" ")
        else:
            print(f'{ch} is not a valid character')
