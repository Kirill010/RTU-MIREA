package GUI;

import Items.Dish;
import Items.Drink;
import Items.DrinkTypeENUM;
import Items.Item;
import Orders.InternetOrderManager;
import Orders.OrderManager;
import Orders.TableOrdersManager;

import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GUI {
	public static final Item[] ITEMS = {
			new Dish("Салат Цезарь", "Назвали в честь Юлия Цезаря", 25),
			new Dish("Стейк на гриле", "Прожарка на выбор", 30),
			new Dish("Буйабес", "Приплыл с самой Франции", 23),
			new Dish("Рататуй", "Сама крыса Реми приготовила", 17),
			new Dish("Наполеон", "Который Бонапарт", 5),
			new Dish("Пицца Дьявол", "Острая пицца", 12),
			new Drink("Зеленый чай", "Успокаивает", 5, DrinkTypeENUM.GREEN_TEA),
			new Drink("Сок яблочный", "Свежевыжатый", 6, DrinkTypeENUM.JUICE),
			new Drink("Сок вишневый", "Свежевыжатый", 6, DrinkTypeENUM.JUICE),
			new Drink("Виски", "Самый лучший виски - это скотч!", 20, 40.0, DrinkTypeENUM.WHISKEY),
			new Drink("Водка", "За здоровье!", 10, 4.7, DrinkTypeENUM.VODKA),
			new Drink("Вода", "ЗОЖ", 1, DrinkTypeENUM.WATER),
			new Drink("Латте", "Кофе с пенкой", 2, DrinkTypeENUM.COFFEE),
	};
	public static InternetOrderManager internetOrderManager = new InternetOrderManager();
	public static TableOrdersManager tableOrderManager = new TableOrdersManager();

	public static void main(String[] args) {
		JFrame frame = new JFrame("Ресторан");
		frame.setSize(600, 300);
		frame.setResizable(false);
		frame.setVisible(true);
		frame.setLayout(null);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JLabel name = new JLabel("Добро пожаловать в наш ресторан");
		name.setSize(500, 30);
		name.setLocation(150, 10);

		JLabel label = new JLabel("Выберите способ оформления заказа: ");
		label.setBounds(150, 50, 300, 20);


		JButton button = new JButton("Ресторан");
		button.setSize(200, 40);
		button.setLocation(300, 100);
		button.setFocusable(false);

		JButton button1 = new JButton("Интернет-заказ");
		button1.setSize(200, 40);
		button1.setLocation(10, 100);

		button1.setFocusable(false);


		frame.add(name);
		frame.add(button);
		frame.add(button1);
		frame.add(label);

		button.addActionListener(e -> {
			frame.dispose();
			TableAuthGui authGUI = new TableAuthGui();
		});

		button1.addActionListener(e -> {
			frame.dispose();
			AuthGUI authGUI = new AuthGUI();
		});

	}
}
