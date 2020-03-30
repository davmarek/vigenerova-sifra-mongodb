# by David MAREK / 30.03.2020
# install pymongo
import pymongo

# PROMĚNNÉ
# NÁZEV DB
DBNAME = "dmdb"
# NÁZEV KOLEKCE
COLNAME = "vigenerova-sifra"


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
    pwd = generate_pwd(PWD, len(TEXT))
    text = ""

    for i, ch in enumerate(cipher):
        ch_int = ord(ch)  # hodnota charu
        increment = ord(pwd[i]) - 96  # hodnota charu hesla - hodnota charu '

        ch_int = ch_int - increment

        # změnšení hodnoty v případě že je větší než hodnota "z"
        if ch_int < 97:
            ch_int = ch_int + 26

        text = text + chr(ch_int)

    return text


# Původní text od uživatele
TEXT = input("Zadej text, který chceš zašifrovat:").lower()
# Heslo od uživatele
PWD = input("Zvol si heslo pro zašifrování:")
# Heslo prodloužené na délku textu
PWD_EXT = generate_pwd(PWD, len(TEXT))

print(f"Váš původní text je: {TEXT}")
print(f"Vaše heslo je: {PWD_EXT}")

# Zašifrovaný text pomocí hesla
CIPHER = cipher_text(TEXT, PWD)
print(f"Zašifrovaný text je: {CIPHER}")

# NAPOJENÍ NA MongoDB CLIENTA
client = pymongo.MongoClient(host="localhost", port=27017)

# VYBRÁNÍ DATABÁZE
db = client[DBNAME]

# VYBRÁNÍ KOLEKCE
col = db[COLNAME]


TEXT = decipher_text(CIPHER, PWD)
print(f"Dešifrovaný text je: {TEXT}")
