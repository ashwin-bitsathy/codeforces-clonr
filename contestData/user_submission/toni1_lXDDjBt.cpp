
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
       int a,b,c=0;
       cin>>a>>b;
       int ac[n];
       for(int i=1;i<=n;i++)
       {
           cin>>ac[i];

       }
       if(ac[b]%2==0){cout<<"yes"<<endl;}
       else{cout<<"no"<<endl;}

    }
    return 0;
}
