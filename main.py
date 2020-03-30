import pymongo


def generate_pwd(original, length):
    pwd = original
    while len(pwd) < length:
        pwd = pwd + original
    return pwd[:length].lower()


def cipher_text(text, pwd):
    text = text.lower()
    print("Váš původní text je: " + text)
    pwd = generate_pwd(pwd, len(text))
    print("Vaše heslo je: " + pwd)
    cipher = ""

    for i, ch in enumerate(text):
        ch_int = ord(ch)  # hodnota charu
        increment = ord(pwd[i]) - 96  # hodnota charu hesla - hodnota charu "a"

        ch_int = ch_int + increment

        # změnšení hodnoty v případě že je větší než hodnota "z"
        if ch_int > 122:
            ch_int = ch_int - 26

        cipher = cipher + chr(ch_int)

    return cipher


def decipher_text(cipher, pwd):
    pass


TEXT = input("Zadej text, který chceš zašifrovat:")
PWD = input("Zvol si heslo pro zašifrování:")

print(cipher_text(TEXT, PWD))
