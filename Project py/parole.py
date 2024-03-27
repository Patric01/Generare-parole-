import random
import string

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=False):
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    if not chars:
        print("Trebuie să alegeți cel puțin un tip de caracter.")
        return None

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Bine ați venit în aplicația de generare a parolelor securizate!")
    length = int(input("Introduceți lungimea parolei: "))
    uppercase = input("Includem litere mari? (da/nu): ").lower() == 'da'
    lowercase = input("Includem litere mici? (da/nu): ").lower() == 'da'
    digits = input("Includem cifre? (da/nu): ").lower() == 'da'
    special_chars = input("Includem caractere speciale? (da/nu): ").lower() == 'da'

    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    if password:
        print("Parola generată este:", password)

if __name__ == "__main__":
    main()
