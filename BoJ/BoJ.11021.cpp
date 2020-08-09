#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	int i = 0;

	for (i = 0; i < t; i++)
	{
		int a, b, sum;
		cin >> a >> b;
		sum = a + b;

		cout << "Case " << "#" << i + 1 << ": " << sum << "\n";
	}
}