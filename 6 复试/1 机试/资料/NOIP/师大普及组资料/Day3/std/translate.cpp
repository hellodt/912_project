#include<bits/stdc++.h>
using namespace std;
int n, m, x, L, R, ans, memory[1010], word[1010];
int main()
{
	freopen("translate.in", "r", stdin);
	freopen("translate.out", "w", stdout); 
	scanf("%d%d", &m, &n);
	for (int i = 1; i <= n; i ++)
	{
		scanf("%d", &x);
		if (!memory[x])  //���� x�����ڴ��� 
		{
			ans ++; R ++; 
			word[R] = x;   //������˳���¼���� x
			memory[x] = 1;   //Ͱ��˼�룬��¼���� x�ѳ������ڴ���
			if (R > m)   //�ڴ����� 
				L ++, memory[word[L]] = 0;  //ɾ���ײ��ĵ���
		}
	}
	printf("%d", ans);
	return 0;
 } 
