package factory;

public class Client {
    Chair chair;

    public void sit(Chair chair) {
        chair.sitOn();
    }

    public void setChair(Chair chair) {
        this.chair = chair;
    }
}
