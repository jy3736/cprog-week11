from time import sleep
import sys
import os
import subprocess
import re
from random import randint


def dump(dat, wd=5, col=5):
    s = ""
    cnt = 0
    for v in dat:
        s += f"{v:{wd}}"
        cnt += 1
        if cnt % col == 0:
            s += "\n"
    return s


def expected():
    dat = [randint(1, 100) for _ in range(randint(10, 20))]
    s = dump(dat)
    s += f"\n{dump(dat,wd=10)}"
    s += f"\n{dump(dat,10,3)}"
    sdat = " ".join([str(_) for _ in dat])
    return sdat, s


def cleanup(s):
    r = s.strip()
    r = [line.strip() for line in r.split("\n")]
    noblk = []
    for l in r:
        if len(l) != 0:
            noblk.append(l)
    return noblk


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
    root = "./src/hw03"
    if sys.platform in ["win32"]:
        root = "."
    # cwd = os.path.abspath(os.getcwd())
    for i in range(10):
        dat, exp = expected()
        ret = test01(execMain(f'{root}/main', dat), exp)
    print("測試通過!")
    print(f"\n{ret}")
    exit(0)


if __name__ == "__main__":
    main()
