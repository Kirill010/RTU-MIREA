package mirea.gui;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

class FIFA extends JFrame {
    int milanCnt = 0;
    int madridCnt = 0;
    JButton milan = new JButton("AC Milan");
    JButton madrid = new JButton("Real Madrid");
    JLabel result = new JLabel("Result: 0 X 0");
    JLabel lastScorer = new JLabel("Last Scorer: N/A");
    Label winner = new Label("Winner: DRAW");

    Font fnt1 = new Font("Times new roman", Font.BOLD, 25);
    Font fnt2 = new Font("Serif", Font.BOLD, 25);

    public FIFA() {
        super("Football Game");
        setSize(300, 300);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        milan.setFont(fnt1);
        madrid.setFont(fnt1);
        result.setFont(fnt1);
        lastScorer.setFont(fnt1);
        winner.setFont(fnt2);
        milan.setBorderPainted(false);
        milan.setFocusPainted(false);
        milan.setBackground(Color.RED);
        milan.setForeground(Color.BLACK);
        madrid.setBorderPainted(false);
        madrid.setFocusPainted(false);
        madrid.setBackground(Color.WHITE);
        madrid.setForeground(Color.BLUE);
        add(milan);
        add(madrid);
        add(result);
        add(lastScorer);
        add(winner);
        milan.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                milanCnt++;
                result.setText("Result: " + milanCnt + " X " + madridCnt);
                lastScorer.setText("Last Scorer: AC Milan");
                if (milanCnt == madridCnt)
                    winner.setText("Winner: DRAW");
                else if (milanCnt > madridCnt)
                    winner.setText("Winner: AC Milan");
                else
                    winner.setText("Winner: Real Madrid");
            }
        });
        madrid.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                madridCnt++;
                result.setText("Result: " + milanCnt + " X " + madridCnt);
                lastScorer.setText("Last Scorer: Real Madrid");
                if (milanCnt == madridCnt)
                    winner.setText("Winner: DRAW");
                else if (milanCnt > madridCnt)
                    winner.setText("Winner: AC Milan");
                else
                    winner.setText("Winner: Real Madrid");
            }
        });
    }

    public static void main(String[] args) {
        new FIFA().setVisible(true);
    }
}