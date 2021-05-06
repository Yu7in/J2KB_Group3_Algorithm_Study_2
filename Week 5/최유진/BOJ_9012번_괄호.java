// BOJ_9012번_괄호

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			String str = br.readLine();
			boolean check = true;
			Stack<Character> s = new Stack<>();
			for (int i = 0; i < str.length(); i++) {
				char ch = str.charAt(i);

				if (s.isEmpty() && ch == ')') {
					check = false;
					break;
				}

				if (ch == '(') {
					s.add(ch);
				} else {
					s.pop();
				}
			}

			if (check && !s.isEmpty()) {
				check = false;
			}

			if (check) {
				sb.append("YES").append("\n");
			} else {
				sb.append("NO").append("\n");
			}
		}
		System.out.println(sb);
	}
}
