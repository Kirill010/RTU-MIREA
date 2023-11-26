package human;

public class HumanTest {
    public static void main(String[] args){
        Human human = new Human("Кирилл", 18);
        human.set_age(19);
        System.out.println(human);

        Human.Head human_head = human.new Head();
        human_head.h(true);
        Human.Hand human_hand = human.new Hand();
        human_hand.c(false);
        Human.Leg human_leg = human.new Leg();
        human_leg.k(false);
    }
}
