#include<bits/stdc++.h>
using namespace std;


class Student{
    public:
        int id;
        double gpa;
};
int main(){
    Student Maruf;
    Maruf.id = 144;
    Maruf.gpa = 3.75;

    cout<<Maruf.id<<" "<<Maruf.gpa<<endl;
    return 0;
}