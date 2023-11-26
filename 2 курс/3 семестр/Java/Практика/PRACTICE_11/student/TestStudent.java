package student;

public class TestStudent {
    public static void main(String[] args) {
        Student[] students = {
                new Student(10, "Кирилл"),
                new Student(19, "Дима"),
                new Student(17, "Сеня"),
                new Student(5, "Тёма"),
                new Student(0, "Богдан")
        };
        for (Student s : students) {
            System.out.println(s);
        }
        selectionSort(students);

        System.out.println();

        for (Student s : students) {
            System.out.println(s);
        }
    }

    public static void selectionSort (Student[] list) {
        int min;
        for (int index = 0; index < list.length - 1; index++) {
            min = index;
            Student tmp = list[index];
            for (int scan = index + 1; scan < list.length; scan++) {
                if (list[scan].compareTo(list[min]) < 0) {
                    min = scan;
                }
                tmp = list[min];
                list[min] = list[index];
                list[index] = tmp;
            }
        }
    }
}
