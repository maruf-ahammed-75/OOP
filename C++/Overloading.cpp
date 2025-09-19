#include<bits/stdc++.h>
using namespace std;


class Student {
    public : 
        int id;
        double gpa;

        Student(int x, double y){
            id = x;
            gpa = y;
        }

        //overloading
        Student(){
            cout<<"overloading Constructor Called"<<endl;
        }

        void display(){
            cout<<id<<" "<<gpa<<endl;
        }
        
};
int main(){
    Student Maruf(144,3.75),ayhan(101,3.85),nayeem;
    Maruf.display();
    ayhan.display();

   

    
    return 0;
}