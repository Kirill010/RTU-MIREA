package GUI;

import Customer.Address;
import Customer.Customer;
import Exceptions.IllegalTableNumber;
import Exceptions.OrderAlreadyAddedException;
import Items.Dish;
import Items.Drink;
import Items.DrinkTypeENUM;
import Items.Item;
import Orders.InternetOrder;
import Orders.TableOrder;
import Orders.TableOrdersManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Objects;

public class TableOrderGUI {
	private JFrame mainFrame;
	private TableOrder order;
	private TableOrdersManager ordersManager;
	private JTextArea mainOrder;
	private JComboBox<Item> comboBox;
	private JLabel totalCostLabel;
	Item[] items = GUI.ITEMS;

	private void setFrame() {
		mainFrame = new JFrame("Table order");
		mainFrame.setSize(1000, 800);
		mainFrame.setLayout(null);
		mainFrame.setVisible(true);
		mainFrame.setResizable(false);
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public TableOrderGUI(Customer customer) {
		setFrame();
		order = new TableOrder(customer);
		ordersManager = new TableOrdersManager();
		JLabel name = new JLabel();
		name.setSize(100, 20);
		name.setLocation(20, 20);
		name.setText("Имя: " + customer.getFirstName());
		mainFrame.add(name);

		JLabel surName = new JLabel();
		surName.setSize(300, 20);
		surName.setLocation(20, 40);
		surName.setText("Фамилия: " + customer.getSecond());
		mainFrame.add(surName);

		JLabel age = new JLabel();
		age.setSize(100, 20);
		age.setLocation(20, 60);
		age.setText("Возраст: " + customer.getAge());
		mainFrame.add(age);

		int freeTable = ordersManager.freeTableNumber();
		if (freeTable == -1) {
			JOptionPane.showMessageDialog(null, "Нет свободных столов", "Приходите позже", JOptionPane.PLAIN_MESSAGE);
			mainFrame.dispose();
		}
		JLabel tableNumber = new JLabel("Столик: " + freeTable);
		tableNumber.setSize(100, 20);
		tableNumber.setLocation(20, 80);
		mainFrame.add(tableNumber);

		totalCostLabel = new JLabel("Всего: 0$");
		totalCostLabel.setSize(200, 25);
		totalCostLabel.setLocation(20, 100);
		mainFrame.add(totalCostLabel);

		JLabel menuLabel = new JLabel("Выберите блюда:");
		menuLabel.setSize(300, 25);
		menuLabel.setLocation(200, 10);
		mainFrame.add(menuLabel);

		comboBox = new JComboBox<Item>(items);
		comboBox.setSize(600, 50);
		comboBox.setLocation(200, 40);
		mainFrame.add(comboBox);

		JButton addItemButton = new JButton("Добавить");
		addItemButton.setSize(130, 30);
		addItemButton.setLocation(200, 120);
		addItemButton.setFocusable(false);
		mainFrame.add(addItemButton);

		addItemButton.addActionListener(e -> {
			try {
				Drink drink = (Drink) comboBox.getSelectedItem();
				if (customer.getAge() < 18 && Objects.requireNonNull(drink).isAlcoholicDrink()) {
					JOptionPane.showMessageDialog(null, "Вам еще нет 18!", "Нельзя", JOptionPane.WARNING_MESSAGE);
					return;
				}
			} catch (Exception ex) {
			}
			order.add((Item) comboBox.getSelectedItem());
			refactorMainOrderTextArea();

		});

		JButton removeItemButton = new JButton("Удалить");
		removeItemButton.setSize(100, 30);
		removeItemButton.setLocation(340, 120);
		removeItemButton.setFocusable(false);
		mainFrame.add(removeItemButton);

		removeItemButton.addActionListener(e -> {

			order.remove((Item) Objects.requireNonNull(comboBox.getSelectedItem()));
			mainOrder.setText("Ваш заказ:\n");
			refactorMainOrderTextArea();
		});

		mainOrder = new JTextArea("Ваш заказ:\n");
		mainOrder.setSize(600, 700);
		mainOrder.setLocation(200, 160);
		mainOrder.setEditable(false);
		mainFrame.add(mainOrder);

		JButton acceptOrderButton = new JButton("Подтвердить");
		acceptOrderButton.setSize(180, 40);
		acceptOrderButton.setLocation(20, 700);
		acceptOrderButton.setFocusable(false);
		mainFrame.add(acceptOrderButton);

		acceptOrderButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (order.getSize() < 1) {
					JOptionPane.showMessageDialog(null, "Вы ничего не заказали", "Ошибка", JOptionPane.PLAIN_MESSAGE);
				} else {
					JOptionPane.showMessageDialog(null, "Ваш заказ скоро принесут наши официанты!", "Подтверждено", JOptionPane.PLAIN_MESSAGE);
					order = new TableOrder(customer);
					try {
						GUI.tableOrderManager.add(order, freeTable);
					} catch (IllegalTableNumber | OrderAlreadyAddedException ex) {
						ex.printStackTrace();
					}
					mainOrder.setText("Заказ оформлен! Приятного аппетита!");
					totalCostLabel.setText("Всего: 0$");
				}
			}
		});


	}

	public void refactorMainOrderTextArea() {
		Item[] currentItems = order.getItems();
		mainOrder.setText("Ваш заказ:\n");
		for (Item item : currentItems) {
			mainOrder.append("\n" + item.toString() + "\n");
		}
		totalCostLabel.setText("Всего: " + order.costTotal() + "$");
	}

	public static void main(String[] args) {
		Address address = new Address("Москва,Борисовские прдуы,115211,14,99,1");
		TableOrderGUI tableOrderGUI = new TableOrderGUI(new Customer("Sam", "Winchester", 16, address));
	}

}
