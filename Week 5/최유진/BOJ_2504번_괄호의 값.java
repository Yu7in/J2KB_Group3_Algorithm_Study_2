// BOJ_2504번_괄호의 값

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String str = br.readLine();
		Stack<Node> s = new Stack<>();
		Stack<Calculate> cal = new Stack<>();
		for (int i = 0; i < str.length(); i++) {
			char ch = str.charAt(i);

			if (s.isEmpty() && (ch == ')' || ch == ']')) {
				cal.add(new Calculate(0, 0, 0));
				break;
			}

			if (ch == '(' || ch == '[') {
				s.add(new Node(ch, i));
			} else {
				Node n = s.pop();
				if (n.ch == '(' && ch == ')') {
					if (cal.isEmpty()) {
						cal.add(new Calculate(2, n.idx, i));
					} else {
						Calculate tmp = cal.pop();
						if (tmp.left - 1 == n.idx && tmp.right + 1 == i) {
							cal.add(new Calculate(tmp.num * 2, n.idx, i));
						} else {
							cal.add(tmp);
							cal.add(new Calculate(2, n.idx, i));
						}
					}
				} else if (n.ch == '[' && ch == ']') {
					if (cal.isEmpty()) {
						cal.add(new Calculate(3, n.idx, i));
					} else {
						Calculate tmp = cal.pop();
						if (tmp.left - 1 == n.idx && tmp.right + 1 == i) {
							cal.add(new Calculate(tmp.num * 3, n.idx, i));
						} else {
							cal.add(tmp);
							cal.add(new Calculate(3, n.idx, i));
						}
					}
				} else {
					cal.add(new Calculate(0, 0, 0));
					break;
				}

				while (cal.size() > 1) {
					Calculate c1 = cal.pop();
					Calculate c2 = cal.pop();
					if (c1.left - 1 == c2.right) {
						cal.add(new Calculate(c1.num + c2.num, c2.left, c1.right));
					} else {
						cal.add(c2);
						cal.add(c1);
						break;
					}
				}
			}
		}

		if (!s.isEmpty()) {
			cal.add(new Calculate(0, 0, 0));
		}

		Calculate ans = cal.pop();
		System.out.println(ans.num);
	}

	public static class Node {
		char ch;
		int idx;

		public Node(char ch, int idx) {
			this.ch = ch;
			this.idx = idx;
		}
	}

	public static class Calculate {
		int num;
		int left;
		int right;

		public Calculate(int num, int left, int right) {
			this.num = num;
			this.left = left;
			this.right = right;
		}
	}
}
