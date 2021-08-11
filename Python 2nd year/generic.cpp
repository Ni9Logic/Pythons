#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> vect;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        vect.push_back(num);
    }
    //? Sorting begins
    int key, j;
    for (int i = 1; i < n; i++)
    {

        key = vect[i];
        j = i - 1;

        /* Move elements of vect[0..i-1], that are
        greater than key, to one position ahead
        of their current position */
        while (j >= 0 && vect[j] > key)
        {
            vect[j + 1] = vect[j];
            j = j - 1;
        }
        vect[j + 1] = key;
    }
    //! Printing out sorted vect!
    for (int i = 0; i < n; i++)
        cout << vect[i] << " ";
}