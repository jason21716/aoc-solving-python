import hashlib

SECRET_KEY = "bgvyzdsv"


def find_passcode(target_zero: int):
    m = hashlib.md5()
    m.update(SECRET_KEY.encode("utf8"))

    passcode = 0
    target_string = "0" * target_zero
    while True:
        m_copy = m.copy()
        m_copy.update(str(passcode).encode("utf8"))
        hex_str = m_copy.hexdigest()
        if hex_str.startswith(target_string):
            break
        passcode += 1
    return passcode


def main_1():
    return find_passcode(5)


def main_2():
    return find_passcode(6)


def performance():
    main_1()
    main_2()
