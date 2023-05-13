package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나:");
		lblMine.setBounds(29, 35, 83, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴:");
		lblCom.setBounds(29, 79, 83, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과:");
		lblResult.setBounds(29, 117, 83, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(115, 32, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(115, 76, 116, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(115, 114, 116, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				myclick();
			}

		
		});
		btn.setBounds(29, 158, 202, 23);
		contentPane.add(btn);
	}
		private void myclick() {
		

			String mine = "";
			String com = "";
			String result = "";

					
			mine = tfMine.getText();
			
			double rnd = Math.random();
			
			if(rnd > 0.5) {
				com = "홀"; 
			} else {
				com = "짝"; 
			}
	
			if(com.equals(mine)) {
				result= "승리";
			} else {
				result= "패배";
			}
				
			tfCom.setText(com);
			tfResult.setText(result);
		}
}
