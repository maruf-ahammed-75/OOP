public class student {
    String name;//instance variable
    int age;
    static String Uniname="UAP";//static variable

    student(String name,int age){
        this.name=name;
        this.age=age;   
    }
    void display(){
        System.out.println("Name: "+name+" Age: "+age+" University Name: "+Uniname);
    }
}
