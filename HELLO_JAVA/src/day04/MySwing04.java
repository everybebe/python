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
import java.util.Iterator;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private final JButton btn = new JButton("까지 합은");
	private JTextField tf4;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 607, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(38, 29, 64, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl = new JLabel("에서");
		lbl.setBounds(114, 32, 57, 15);
		contentPane.add(lbl);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(169, 29, 64, 21);
		contentPane.add(tf2);
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				myclick();
			}

			
		});
		btn.setBounds(259, 24, 102, 31);
		contentPane.add(btn);
		
		tf4 = new JTextField();
		tf4.setBounds(377, 29, 116, 21);
		contentPane.add(tf4);
		tf4.setColumns(10);
	}

	private void myclick() {
		String num1 = tf1.getText();
		String num2 = tf2.getText();
		int sum = 0;
		
		int a = Integer.parseInt(num1);
		int b = Integer.parseInt(num2);
		
		for(int i=a; i<=b; i++) {
			sum += i;
		}
		
		tf4.setText(sum+"");
	}
}
