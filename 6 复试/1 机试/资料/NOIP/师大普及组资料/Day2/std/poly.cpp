#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("poly.in", "r", stdin);
	freopen("poly.out", "w", stdout);
    int n, a;
    cin >> n;
    for(int i = n; i >= 0; i --)
	{
        cin >> a;
        if (a)   //�� 0ϵ��
		{    
            if (i != n && a > 0) cout << "+";    //�����������Ƿ�Ϊ��ߴ�������Ӻ�
            if (abs(a) > 1 || i == 0) cout << a;    //���ϵ����ϵ����Ϊ����1��ָ��Ϊ0��
            if (a == -1 && i) cout << "-";    //-1ϵ�����У�������������
            if (i > 1) cout << "x^" << i;    //���μ��������ָ��
            if (i == 1) cout << "x";    //һ����
        }
    }
    return 0;
}
