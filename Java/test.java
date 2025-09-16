//object create
//program run korar jonno main method lagbe

// package oop;

public class test{
    public static void main(String[] args) {
        //object declaration
        Teacher Arnob;//class type ar variable

        //object creation
        Arnob = new Teacher();//new keyword diye object create

        Arnob.name = "Arnob";
        Arnob.age = 30;
        Arnob.phone = "017xxxxxxxx";


        //aksthe
        // Teacher Plabon = new Teacher();

        System.out.println("name = "+Arnob.name);
        System.out.println("age = "+Arnob.age);
        System.out.println("phone = "+Arnob.phone);
    }
}