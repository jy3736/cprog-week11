from time import sleep
import sys
import os
import subprocess
import re
import random


def expected():
    n = random.randint(1, 10)
    s = "*"*20+"\n"
    sym = "*"
    if n % 2 == 0:
        sym = "#"
    for i in range(1, n+1):
        s += sym*i+"\n"
    s += "*"*20+"\n"
    return f"{n}", s


def cleanup(s):
    r = s.strip()
    r = [line.strip() for line in r.split("\n")]
    return r


def failed(c, e):
    print(f"Your Output : {c}")
    print(f"Expected    : {e}")
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
    root = "./src/hw02"
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
