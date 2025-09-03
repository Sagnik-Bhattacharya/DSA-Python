#include <bits/stdc++.h>
using namespace std;
int main(){
    long long n,t;
    cin>>n>>t;
    vector<long long> a(n);
    for(long long i=0;i<n;i++){
        cin>>a[i];
    }

    long long l=0;
    long long r=1e18;
    while(r-l>1){
        long long m=(l+r)/2;
        long long cnt=0;
        for(long long i=0;i<n;i++){
            cnt+=m/a[i];
        }

        if(cnt>=t) r=m;
        else l=m;
    }
    cout<<r<<endl;
}