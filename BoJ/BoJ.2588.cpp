#include <iostream>
using namespace std;

int main()
{
	int n, m;
	cin >> n;
	cin >> m;
	
	int a, b, c, d;
	a = (n) * ((m % 100) % 10);
	b = (n) * ((m / 10) % 10);
	c = (n) * (m / 100);
	d = n * m;

	cout << a << endl;
	cout << b << endl;
	cout << c << endl;
	cout << d ;

	return 0;
}