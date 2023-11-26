package file;

public class TestFile {
    public static void main(String[] args) {

        String name_txt = "C:\\Users\\super\\IdeaProjects\\MIREA\\practice__13\\src\\file\\pr13.txt";

        File task = new File();
        System.out.println("1: Реализовать запись в файл введённой с клавиатуры информации");
        task.t_1(name_txt);
        System.out.println("2: Реализовать вывод информации из файла на экран");
        task.t_2(name_txt);
        System.out.println('\n' + "3: Заменить информацию в файле на информацию, введённую с клавиатуры");
        task.t_1(name_txt);
        System.out.println("4: Добавить в конец исходного файла текст, введённый с клавиатуры");
        task.t_4(name_txt);
        System.out.println("Result");
        task.t_2(name_txt);

    }
}
