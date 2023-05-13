package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JTextField tf4;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 648, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(28, 37, 56, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(135, 37, 56, 21);
		contentPane.add(tf2);
		
		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(239, 37, 56, 21);
		contentPane.add(tf3);
		
		tf4 = new JTextField();
		tf4.setColumns(10);
		tf4.setBounds(449, 37, 56, 21);
		contentPane.add(tf4);
		
		JLabel lbl1 = new JLabel("에서");
		lbl1.setBounds(96, 40, 57, 15);
		contentPane.add(lbl1);
		
		JLabel lbl2 = new JLabel("까지");
		lbl2.setBounds(203, 40, 57, 15);
		contentPane.add(lbl2);
		
		JButton btn = new JButton("배수의합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				myclick();
			}

		});
		btn.setBounds(307, 36, 130, 23);
		contentPane.add(btn);
	}
	
	

	private void myclick() {

			String num1 = tf1.getText();
			String num2 = tf2.getText();
			String num3 = tf3.getText();
			
			int num11 = Integer.parseInt(num1);
			int num22 = Integer.parseInt(num2);
			int num33 = Integer.parseInt(num3);
			
			int sum = 0;
			
			for(int i=num11; i<=num22; i++) {
				if(i % num33 == 0) {
				sum += i;
			}
			
	}
			tf4.setText(sum+"");	
}
}
