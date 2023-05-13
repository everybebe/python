package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.Label;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing11 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;
	
	String com = "123";
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing11 frame = new MySwing11();
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
	public MySwing11() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 329, 506);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("야구게임");
		lbl.setBounds(23, 36, 88, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(123, 33, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");

		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				myclick();
			}
			
			
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
			}
			
		});
		btn.setBounds(23, 75, 216, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(23, 107, 216, 324);
		contentPane.add(ta);
		
		setRandomCom();
	}
	
	public void setRandomCom() {
		
		String[] arr = {"0","1","2","3","4","5","6","7","8","9"};
		
				
		for(int i=0; i<10; i++) {
			int ran = (int) (Math.random()*9);
			
			String a = arr[ran];
			String b = arr[0];
			arr[0] = a;
			arr[ran] = b;
		}
		
	com = arr[0] + arr[1] + arr[2];
	System.out.println("com" + com);
		
	}
	
	
	//private void myclick(String[] arr) {


		//테스트
		//String result = arr[0]+"" + arr[1]+"" + arr[2];
		//ta.setText(result);

		/*
			String a = tf.getText();
			String[] aa = a.split("");
			String currentText = ta.getText();
			int strike=0;
			int ball=0;
			
			for(int i=0; i<3; i++) {
				for(int j=0; j<3; j++) {
					if(aa[i].equals(arr[j]) && i==j ){
						strike++;
					}else if(aa[i].equals(arr[j]) && i!=j ){
						ball++;
					}
				}
			}
		
			if(strike==3) {
				ta.setText(currentText+"\n"+a+"___"+strike+"s"+ball+"b\n"+"게임종료");
			}else {
			ta.setText(currentText+"\n"+ a+"___"+strike+"s"+ball+"b");
			}
		
		 */
	//}
	
	public void myclick() {
		String mine = tf.getText();
		
		int s = 0;
		
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		if(c1.equals(m1)) {s++;} 
		if(c2.equals(m2)) {s++;} 
		if(c3.equals(m3)) {s++;} 

		System.out.println(s);
		
		int b =0;
		if(c1.equals(m2)||c1.equals(m3))  { b++;}
		if(c2.equals(m1)||c1.equals(m3))  { b++;}
		if(c3.equals(m1)||c1.equals(m2))  { b++;}
		
		String str_new = mine+"\t"+s+"S"+b+"b"+"\n"; 
		String str_old = ta.getText();
		
		ta.setText(str_old+str_new);
		tf.setText("");
		
		if(s==3) {
		JOptionPane.showMessageDialog(null, "정답입니다.");
		}
	}

	
}	
	
//	private String str(int i) {
//		return null;
//	}
	
	

