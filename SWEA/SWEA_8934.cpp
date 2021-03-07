#include<iostream>
#include<string>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{	
		string s;
		cin >> s;
		int qa = 0;
		int qb = 0;
		int qc = 0;

		for (int j = 0; j < s.size(); j++)
		{	
			if (s[j] == 'a')
				qa = qa + 1;
			else if (s[j] == 'b')
				qb = qb + 1;
			else if (s[j] == 'c')
				qc = qc + 1;

			if (qa >= 1 && qb >=1 && qc >= 1)
			{
				qa = qa - 1;
				qb = qb - 1;
				qc = qc - 1;
			}
		}

		// cout << qa << qb << qc << "\n";

		int qq = qa + qb + qc;
		if (qq == 0 || qq == 1)
		{
			cout << "#" << test_case << " YES" << "\n";
			continue;
		}
		else if ((qa == 0 && qb == 1 && qc == 1) || (qa == 1 && qb == 0 && qc == 1) || (qa == 1 && qb == 1 && qc == 0))
		{
			cout << "#" << test_case << " YES" << "\n";
			continue;
		}

		cout << "#" << test_case << " NO" << "\n";

	}
	return 0; //정상종료시 반드시 0을 리턴해야합니다.
}