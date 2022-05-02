## 選擇輸出 1 ~ n 中全部整數、偶數、奇數、及被4整除的整數。

- 這是期中考題目的再進化，將期中考第3題的加分題，以函數的方式設計。
- 經由標準輸入(stdin)給定兩個參數：功能選擇及n
    - 功能選擇 = 0：輸出 1 ~ n 全部整數。
    - 功能選擇 = 1：輸出 1 ~ n 中的偶數。
    - 功能選擇 = 2：輸出 1 ~ n 中的奇數。
    - 功能選擇 = 3：輸出 1 ~ n 中可被4整除的整數。
- 對應『功能選擇』的函數依序為：printAll(int)、printEven(int)、printOdd(int)、及printDiv4(int)。

### Test in Windows

```shell
hw01> echo 0 10 | .\main.exe
All     :    1   2   3   4   5   6   7   8   9  10

hw01> echo 1 10 | .\main.exe
Even    :    2   4   6   8  10

hw01> echo 2 10 | .\main.exe
Odd     :    1   3   5   7   9

hw01> echo 3 10 | .\main.exe
Div. 4  :    4   8

hw01> python ..\..\tools\check01.py
測試通過!

Odd     :    1   3   5   7   9  11
hw01> python ..\..\tools\check01.py
測試通過!

Div. 4  :    4   8  12  16
````