package sum;

import java.util.Scanner;

public class Sum {

	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		int a,b;
		System.out.println("Enter the two numbers");
		a=s.nextInt();
		b=s.nextInt();
		int c;
		c=a+b;
		System.out.println("Sum="+c);

	}

}
