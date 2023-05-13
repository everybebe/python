package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {
	JTextArea ta;
	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 488);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수");
		lbl.setBounds(55, 32, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(124, 29, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}

		});
		btn.setBounds(58, 71, 183, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(55, 110, 190, 304);
		contentPane.add(ta);
	}
	

	private void myclick() {

		String a = tf.getText();
		
		int aa = Integer.parseInt(a);
		String result ="";
		
		for(int i=1; i<=9; i++) {
			result += aa + "*" + i + "=" + aa*i + "\n";
		
		}
		
		ta.setText(result);
	
		
}
}