package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class MySwing05 extends JFrame {

	JLabel lbl1;
	JLabel lbl2;
	JLabel lbl3;
	JLabel lbl4;
	JLabel lbl5;
	JLabel lbl6;
	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
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
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl1 = new JLabel("_");
		lbl1.setBounds(40, 10, 18, 15);
		contentPane.add(lbl1);
		
		lbl2 = new JLabel("_");
		lbl2.setBounds(98, 10, 57, 15);
		contentPane.add(lbl2);
		
		lbl3 = new JLabel("_");
		lbl3.setBounds(155, 10, 57, 15);
		contentPane.add(lbl3);
		
		lbl4 = new JLabel("_");
		lbl4.setBounds(224, 10, 57, 15);
		contentPane.add(lbl4);
		
		lbl5 = new JLabel("_");
		lbl5.setBounds(296, 10, 57, 15);
		contentPane.add(lbl5);
		
		lbl6 = new JLabel("_");
		lbl6.setBounds(365, 10, 57, 15);
		contentPane.add(lbl6);
		
		JButton btn = new JButton("로또생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}

			
		});
		btn.setBounds(117, 49, 218, 23);
		contentPane.add(btn);
	}
	
	private void myclick() {
		
		int[] num = new int[45];
		
		for(int i = 1 ; i <=45; i ++) {
			 num[i-1]=i;
		}
		
		
		
		for(int i=1; i<=45; i++) {
			int ran = (int) (Math.random()*46);
			
			int a = num[ran];
			int b = num[0];
			num[0] = a;
			num[ran]= b;
					
		}
		
		lbl1.setText(num[0]+"");
		lbl2.setText(num[1]+"");
		lbl3.setText(num[2]+"");
		lbl4.setText(num[3]+"");
		lbl5.setText(num[4]+"");
		lbl6.setText(num[5]+"");
		
		
	}

}
