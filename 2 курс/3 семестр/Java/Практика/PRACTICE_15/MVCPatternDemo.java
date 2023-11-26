public class MVCPatternDemo {
    private static Student retrieveStudentFromDB() {
        Student student = new Student();
        student.setName("Дин");
        student.setId("001");
        return student;
    }
    public static void main(String[] args) {
        Student model = retrieveStudentFromDB();

        StudentView view = new StudentView();

        StudentController controller = new StudentController(model, view);

        controller.updateView();

        controller.setStudentName("Сэм");
        controller.setStudentId("002");

        controller.updateView();
    }
}