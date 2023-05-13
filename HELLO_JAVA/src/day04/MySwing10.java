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
import java.util.Iterator;

public class MySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tfFirst;
	private JTextField tfLast;
	JTextArea ta;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
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
	public MySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 543);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblFirst = new JLabel("첫별수");
		lblFirst.setBounds(119, 54, 57, 15);
		contentPane.add(lblFirst);
		
		JLabel lblLast = new JLabel("끝별수");
		lblLast.setBounds(119, 95, 57, 15);
		contentPane.add(lblLast);
		
		tfFirst = new JTextField();
		tfFirst.setBounds(219, 51, 116, 21);
		contentPane.add(tfFirst);
		tfFirst.setColumns(10);
		
		tfLast = new JTextField();
		tfLast.setBounds(219, 92, 116, 21);
		contentPane.add(tfLast);
		tfLast.setColumns(10);
		
		JButton btn = new JButton("별 그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}

			
		});
		btn.setBounds(122, 143, 213, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(119, 187, 216, 217);
		contentPane.add(ta);
	}
	
	private void myclick() {
		String a = tfFirst.getText();
		String b = tfLast.getText();
		
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		String result = "";

		for(int i = aa; i<=bb; i++) {
			for(int j=0; j<i; j++) {
			
			result += "*";
		}
			result += "\n";
			ta.setText(result+"");
		}
		
	}
	

}
