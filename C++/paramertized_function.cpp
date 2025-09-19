#include<bits/stdc++.h>
using namespace std;


class Student {
    public : 
        int id;
        double gpa;

        void display(){
            cout<<id<<" "<<gpa<<endl;
        }
        void setValue(int x, double y){
            id = x;
            gpa = y;
        }
};
int main(){
    Student Maruf,ayhan;
    Maruf.setValue(100,3.75);
    Maruf.display();

    ayhan.setValue(101,3.85);
    ayhan.display();
    return 0;
}