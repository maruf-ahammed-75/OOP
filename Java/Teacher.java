// package oop;

public class Teacher{
    String name;
    int age;
    String phone;

    void display(){
        System.out.println("name = "+name);
        System.out.println("age = "+age);
        System.out.println("phone = "+phone);
    }

    void setInfo(String n, int a, String p){
        name = n;
        age = a;
        phone = p;
    }
} 