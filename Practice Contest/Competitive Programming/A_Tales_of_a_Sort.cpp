#include <bits/stdc++.h>
using namespace std;

#define superfast ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define ll long long
#define yes {cout<<"YES"<<endl;}
#define no {cout<<"NO"<<endl;}

/// for loops
#define fori(x) for( int i = 0; i < x; i++)
#define forj(x) for( int j = 0; j < x; j++)

void ans()
{
    int n;
    cin >> n;
    int arr[n];
    int unsortedBigger = 0;

    fori(n) 
    {
        cin >> arr[i];
        if(i >= 1 && arr[i - 1] > arr[i])
        {
            unsortedBigger = max(unsortedBigger, arr[i - 1]);
        }
    }

    cout << unsortedBigger << endl;
}

int main()
{
    superfast
    int t;
    cin >> t;
    while (t--)
    {
        ans();
    }

    return 0;
}