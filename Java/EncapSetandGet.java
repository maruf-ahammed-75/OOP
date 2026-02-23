public class EncapSetandGet {
    private String name;
    private int age;

    void setage(int age){
        this.age = age;
    }
    void setname(String name){
        this.name = name;
    }
    void display(){
        System.out.println("name "+name);
        System.out.println("age "+age);
    }
}
