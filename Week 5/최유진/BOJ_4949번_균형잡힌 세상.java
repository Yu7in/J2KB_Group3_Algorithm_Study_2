// BOJ_4949번_균형잡힌 세상

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		while (true) {
			String str = br.readLine();
			if (str.equals(".")) {
				break;
			}

			boolean check = true;
			Stack<Character> s = new Stack<>();
			for (int i = 0; i < str.length(); i++) {
				char ch = str.charAt(i);
				if (ch == '(' || ch == '[') {
					s.add(ch);
				} else if (ch == ')' || ch == ']') {
					if (s.isEmpty()) {
						check = false;
						break;
					}
					char temp = s.pop();
					if ((temp == '(' && ch == ')') || (temp == '[' && ch == ']')) {
						continue;
					} else {
						check = false;
						break;
					}
				}
			}

			if (!s.isEmpty()) {
				check = false;
			}

			if (check) {
				sb.append("yes").append("\n");
			} else {
				sb.append("no").append("\n");
			}
		}
		System.out.println(sb);
	}
}
