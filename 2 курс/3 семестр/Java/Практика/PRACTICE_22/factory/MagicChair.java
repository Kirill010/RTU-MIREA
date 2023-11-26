package factory;

public class MagicChair implements Chair {

    public void doMagic() {
        System.out.println("Магия совершена!");
    }

    @Override
    public void sitOn() {
        System.out.println("Вы сидите на Магическом стуле");
    }
}
