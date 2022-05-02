from time import sleep
import sys
import os
import subprocess
import re
from random import randint


def expected():
    op, n = randint(0, 3), randint(10, 20)
    dat = range(1, n+1)
    s = ""
    if op == 0:
        s = " ".join([str(_) for _ in dat])
    elif op == 1:
        even = []
        for d in dat:
            if d % 2 == 0:
                even.append(d)
        s = " ".join([str(_) for _ in even])
    elif op == 2:
        odd = []
        for d in dat:
            if d % 2 == 1:
                odd.append(d)
        s = " ".join([str(_) for _ in odd])
    elif op == 3:
        div4 = []
        for d in dat:
            if d % 4 == 0:
                div4.append(d)
        s = " ".join([str(_) for _ in div4])
    return f"{op} {n}", s


def cleanup(s):
    r = s.split(":")[-1]
    r = r.strip()
    r = r.split()
    return r


def failed(c, e):
    print(f"Your Output :\n{c}")
    print(f"Expected    :\n{e}")
    exit(1)


def test01(c, e):
    chk = cleanup(c)
    exp = cleanup(e)
    for a, b in zip(chk, exp):
        if a != b:
            failed(c, e)
    return c


def execMain(cmd, dat=""):
    dat = dat.encode('utf-8')
    p = subprocess.Popen([cmd, ],
                         shell=False,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
                         )
    p.stdin.write(dat)
    output, error = p.communicate()
    output = output.decode('utf-8')
    p.stdin.close()
    return output


def main():
    root = "./src/hw01"
    if sys.platform in ["win32"]:
        root = "."
    # cwd = os.path.abspath(os.getcwd())
    for i in range(20):
        dat, exp = expected()
        ret = test01(execMain(f'{root}/main', dat), exp)
    print("測試通過!")
    print(f"\n{ret}")
    exit(0)


if __name__ == "__main__":
    main()
