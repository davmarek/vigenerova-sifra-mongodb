import pymongo


def generate_pwd(original, length):
    pwd = original
    while len(pwd) < length:
        pwd = pwd + original
    return pwd[:length].lower()


def cipher_text(text, pwd):
    """
    Funkce příjme text, a heslo - např. text=python & heslo=abc
    heslo se pak prodlouží na délku textu funkcí generate_pwd()
    každé písmeno pak textu pak projde úpravou a zapíše se do výsledné šifry
    """
    pwd = generate_pwd(PWD, len(TEXT))
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


TEXT = input("Zadej text, který chceš zašifrovat:").lower()
PWD = input("Zvol si heslo pro zašifrování:")

PWD_EXT = generate_pwd(PWD, len(TEXT))

print(f"Váš původní text je: {TEXT}")
print(f"Vaše heslo je: {PWD_EXT}")

print("Zašifrovaný text je: " + cipher_text(TEXT, PWD_EXT))
