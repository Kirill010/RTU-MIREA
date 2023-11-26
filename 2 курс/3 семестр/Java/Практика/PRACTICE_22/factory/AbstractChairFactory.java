package factory;

public interface AbstractChairFactory {
    VictorianChair createVictorianChair();

    FunctionalChair createFunctionalChair();

    MagicChair createMagicChair();
}
