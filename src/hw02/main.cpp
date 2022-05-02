#include <iostream>
using namespace std;

// add your code here

// ==============================================
// -----vv----- 不得修改『以下』的程式 -----vv-----
// ==============================================

int main()
{
    int n;
    cin >> n;

    drawLine(20);
    for(int i=1; i<=n; i++)
        drawLine(i,(n%2==0)?'#':'*');
    drawLine(20);

    return 0;
}
