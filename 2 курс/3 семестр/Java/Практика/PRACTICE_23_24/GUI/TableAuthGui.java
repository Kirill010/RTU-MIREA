package GUI;

import Customer.Address;
import Customer.Customer;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TableAuthGui {
	JFrame mainFrame;

	private void setFrame() {
		mainFrame = new JFrame("Table authentication");
		mainFrame.setSize(600, 500);
		mainFrame.setLayout(null);
		mainFrame.setVisible(true);
		mainFrame.setResizable(false);
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public TableAuthGui() {
		setFrame();

		JLabel name = new JLabel("Имя");
		name.setSize(100, 40);
		name.setLocation(50, 100);
		mainFrame.add(name);

		JTextField tName = new JTextField();
		tName.setSize(190, 40);
		tName.setLocation(150, 100);
		mainFrame.add(tName);

		JLabel surName = new JLabel("Фамилия");
		surName.setSize(100, 40);
		surName.setLocation(50, 150);
		mainFrame.add(surName);

		JTextField tSurName = new JTextField();
		tSurName.setSize(190, 40);
		tSurName.setLocation(150, 150);
		mainFrame.add(tSurName);

		JLabel age = new JLabel("Возраст");
		age.setSize(100, 40);
		age.setLocation(50, 200);
		mainFrame.add(age);

		JTextField tAge = new JTextField();
		tAge.setSize(100, 40);
		tAge.setLocation(150, 200);
		mainFrame.add(tAge);

		JButton button1 = new JButton("Зарегистрироваться");
		button1.setFocusable(false);
		button1.setSize(300, 40);
		button1.setLocation(150, 400);
		mainFrame.add(button1);

		button1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				String name, surname, addressText;
				int age;
				name = tName.getText();
				surname = tSurName.getText();
				if (!name.isEmpty() && !surname.isEmpty()  && !tAge.getText().isEmpty()) {
					age = Integer.parseInt(tAge.getText());
					Customer me = new Customer(name, surname, age);
					mainFrame.dispose();
					TableOrderGUI tableOrderGUI = new TableOrderGUI(me);
				} else {
					JOptionPane.showMessageDialog(null, "Вы ввели не все данные!", "Warning", JOptionPane.WARNING_MESSAGE);
				}
			}
		});

	}
}
