# include <iostream>
# include <cstring>
using namespace std;

int main()
{
	int n;
	cin >> n;

	for (int i = 0; i < n ; i++)
	{
		for (int j = 1; j<n-i ; j++)
		{
			cout << " ";
		}

		for (int k = 0 ; k <i*2+1 ; k++)
		{
			cout << "*";
		}

		cout << endl;
	}

	int c = 2;
	for (int i = n-1; i > 0 ; i--)
	{

		for (int j = 1; j< c ; j++)
		{
			cout << " ";
		}

		for (int k = 2 * i - 1; k>0 ; k--)
		{
			cout << "*";
		}
		c++;
		if (i != 1)
		{
			cout << endl;
		}

	}
	return 0;
} 