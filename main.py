from loader import words
from loader import cursor
import sys

def trans_word(text):
    if text in words:
        return words[text]
    else:
        return text

def has_result(text: str) -> bool:
    cursor.execute("SELECT count(*) FROM bopomofo WHERE text LIKE ?", [text+'%'])
    res = cursor.fetchone()[0]
    return res > 0

def trans_sentense(text):
    ret = ""
    buf = ""
    for x in text:
        if not has_result(x):
            ret = ret + ' ' + trans_word(buf)
            buf = ""
            ret = ret + ' ' + trans_word(x)
            continue
        if not has_result(buf + x):
            ret = ret + ' ' + trans_word(buf)
            buf = x
        else:
            buf = buf + x
    ret = ret + ' ' + trans_word(buf)
    return ret[1:]

if __name__ == "__main__":
    while True:
        x = input(">>> ")
        print(trans_sentense(x))
