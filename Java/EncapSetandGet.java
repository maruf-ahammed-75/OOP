public class EncapSetandGet {
    private String name;
    private int age;

    void setage(int age){
        this.age = age;
    }
    void setname(String name){
        this.name = name;
    }

    String getname(){
        return name;
    }

    int getage(){
        return age;
    }
    
    void display(){
        System.out.println("name "+name);
        System.out.println("age "+age);
    }
}
