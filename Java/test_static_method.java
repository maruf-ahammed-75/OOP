// package Java;

public class test_static_method {
    public static void main(String[] args) {
        StaticMethod ob1 = new StaticMethod();
        ob1.display(); // Calling non-static method using object
        StaticMethod.staticDisplay(); // Calling static method using class name
    }
}
