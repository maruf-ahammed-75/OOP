
public class EncapTest1 {
    public static void main(String[] args) {
        EncapSetandGet ob1 = new EncapSetandGet();

        ob1.setage(25);
        ob1.setname("Maruf");
        System.out.println("name "+ob1.getname());
        System.out.println("age "+ob1.getage());
        ob1.display();
    }
}
