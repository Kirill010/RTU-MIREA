package GUI;

import Customer.Address;
import Customer.Customer;
import Items.Item;
import Orders.InternetOrderManager;
import Orders.Order;

import javax.swing.*;
import java.awt.*;
import java.util.Arrays;

public class OrderManagerGUI {
	public OrderManagerGUI() {
		JFrame frame = new JFrame("Manager");
		frame.setSize(600, 500);
		frame.setResizable(false);
		frame.setVisible(true);
		frame.setLayout(null);
		frame.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);



		JTextPane internetOrderComboBox = new JTextPane();

		Order[] orders = GUI.internetOrderManager.getOrders();
		StringBuilder item = new StringBuilder();
		for (int i = 0; i < orders.length; i++) {
			Item[] items = orders[i].getItems();
			item.append("Order ").append(i+1).append("\n");
			for(int j = 0; j < items.length; j++) {
				item.append(items[j].toString());
				item.append("\n");
			}
			item.append("\n");
		}

		internetOrderComboBox.setText(item.toString());
		System.out.println(item);
		internetOrderComboBox.setEditable(false);
		internetOrderComboBox.setSize(400, 400);
		internetOrderComboBox.setLocation(0, 20);
		frame.add(internetOrderComboBox);
	}

}
