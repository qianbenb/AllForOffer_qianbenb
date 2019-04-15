# include<iostream>
using
namespace
std;
double ** Map;
int
touch = 0;
int
N, M;
void
typeinmap(double ** Map, int
N, int
M)
{
for (int i = 0; i < N; i++)
{
    cout << "请输入第" << i << "行:" << endl;
for (int j = 0; j < M; j++)
cin >> Map[i][j];
}
}
bool
GoPoint(int
x, int
y, int
fromx, int
fromy, int
Z, int
W)
{
if (x == Z & & y == W)
{
    touch + +;
return true;
}
bool
success = false;
// 访问左边
if (x - 1 >= 0)
{
if (fromx == x - 1 & & fromy == y)
    {
    }
else
    {

    if (Map[x - 1][y] > Map[x][y])
success = GoPoint(x - 1, y, x, y, Z, W);
}
}
// 访问右边
if (x + 1 <= N - 1)
{
if (fromx == x + 1 & & fromy == y)
    {
    }
else
    {

    if (Map[x + 1][y] > Map[x][y])
success = GoPoint(x + 1, y, x, y, Z, W);
}
}
// 访问下边
if (y + 1 <= M - 1)
{
if (fromx == x & & fromy == y + 1)
    {
    }
else
    {
    if (Map[x][y + 1] > Map[x][y])
success = GoPoint(x, y + 1, x, y, Z, W);
}
}
// 访问上边
if (y - 1 >= 0)
{
if (fromx == x & & fromy == y - 1)
    {
    }
else
    {
    if (Map[x][y - 1] > Map[x][y])
success = GoPoint(x, y - 1, x, y, Z, W);
}
}
}
int
CalStart(double ** Map, int
N, int
M, int
X, int
Y, int
Z, int
W)
{
    GoPoint(X, Y, X, Y, Z, W);
cout << touch;
return touch;
}

int
main()
{

cout << "输入行数N,列数M:" << endl;
cin >> N >> M;
Map = new
double * [N];
for (int i = 0; i < N; i++)
    {
        Map[i] = new
    double[M];
    }
    typeinmap(Map, N, M);
    for (int i = 0; i < N; i++)
        {
        for (int j = 0; j < M; j++)
        cout << Map[i][j];
        }
    cout << "请输入初始坐标X,Y.终点坐标Z，W" << endl;
    int
    X, Y, Z, W;
    cin >> X >> Y >> Z >> W;
    cout << CalStart(Map, N, M, X, Y, Z, W) << endl;
    system("pause");
    return 0;
    }

