#include<bits/stdc++.h>
using namespace std;


class Student {
    public : 
        int id;
        double gpa;

        void display(){
            cout<<id<<" "<<gpa<<endl;
        }
};
int main(){
    Student Maruf,ayhan;
    Maruf.id = 144;
    Maruf.gpa = 3.75;
    Maruf.display();

    ayhan.id = 101;
    ayhan.gpa = 3.50;
    ayhan.display();
    return 0;
}