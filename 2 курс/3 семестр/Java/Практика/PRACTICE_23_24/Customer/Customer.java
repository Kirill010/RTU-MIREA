package Customer;


public class Customer {
    private static final Customer MATURE_UNKNOWN_CUSTOMER = new Customer(19);
    private static final Customer NOT_MATURE_UNKNOWN_CUSTOMER = new Customer(16);
    private final String firstName;
    private final String secondName;
    private final int age;
    private final Address address;

    public Customer(String firstName, String secondName, int age, Address address) {
        this.firstName = firstName;
        this.secondName = secondName;
        this.age = age;
        this.address = address;
    }

    public Customer(String firstName, String secondName, int age) {
        this.firstName = firstName;
        this.secondName = secondName;
        this.age = age;
        this.address = null;
    }

    public Customer(int age) {
        this.firstName = "firstName";
        this.secondName = "second";
        this.age = age;
        this.address = new Address();
    }

    public String getFirstName() {
        return firstName;
    }

    public String getSecond() {
        return secondName;
    }

    public int getAge() {
        return age;
    }

    public Address getAddress() {
        return address;
    }
}
