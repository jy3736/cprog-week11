#include <iostream>
#include <iomanip>

using namespace std;

int nthNum(int dat[], int len, int n = 0)
{
    // add your code here
}

// ==============================================
// -----vv----- 不得修改『以下』的程式 -----vv-----
// ==============================================

int main()
{
    int dat[100];
    int cnt = 0;

    while (cin >> dat[cnt++])
        ;
    cnt--;

    cout << nthNum(dat, cnt, 0) << endl;
    cout << nthNum(dat, cnt, 1) << endl;
    cout << nthNum(dat, cnt, cnt / 3) << endl;
    cout << nthNum(dat, cnt, cnt / 2) << endl;
    cout << nthNum(dat, cnt, cnt - 1) << endl;

    return 0;
}
