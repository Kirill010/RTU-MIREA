package human;

public class Human {
    private String name;
    private int age;

    public Human(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String get_name() {
        return this.name;
    }

    public void set_name(String name) {
        this.name = name;
    }

    public int get_age() {
        return this.age;
    }

    public void set_age(int age) {
        if (0 < age && age < 100) {
            this.age = age;
        }
    }

    @Override
    public String toString() {
        return "Имя человека: " + this.name + ", Возраст: " + this.age;
    }

    public class Head {
        private boolean hurt;

        public boolean get_hurt() {
            return this.hurt;
        }

        public void set_hurt(boolean hurt) {
            this.hurt = hurt;
        }

        public void h(boolean hurt) {
            if (hurt) {
                System.out.println("Голова болит");
            }
            else {
                System.out.println("Голова не болит");
            }
        }
    }

    public class Hand {
        private boolean clap;

        public boolean get_clap() {
            return this.clap;
        }

        public void set_clap(boolean clap) {
            this.clap = clap;
        }

        public void c(boolean clap) {
            if (clap) {
                System.out.println("Стоим на руках!");
            }
            else {
                System.out.println("Руки ничего не делают");
            }
        }
    }

    public class Leg {
        private boolean kick;

        public boolean get_kick() {
            return this.kick;
        }

        public void set_kick(boolean kick) {
            this.kick = kick;
        }

        public void k(boolean kick) {
            if (kick) {
                System.out.println("Ногой стучим ритм!");
            }
            else {
                System.out.println("Ноги ничего не делают");
            }
        }
    }
}
