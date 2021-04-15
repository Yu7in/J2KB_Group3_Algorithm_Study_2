// BOJ_1463번_1로 만들기

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int X = Integer.parseInt(br.readLine());
		int[] arr = new int[X + 2];

		for (int i = 2; i < X + 2; i++) {
			arr[i] = i - 1;
		}

		for (int i = 2; i <= X; i++) {
			if (i % 2 == 0) {
				arr[i] = arr[i] > arr[i / 2] + 1 ? arr[i / 2] + 1 : arr[i];
			}
			if (i % 3 == 0) {
				arr[i] = arr[i] > arr[i / 3] + 1 ? arr[i / 3] + 1 : arr[i];
			}
			arr[i] = arr[i] > arr[i - 1] + 1 ? arr[i - 1] + 1 : arr[i];
		}

		System.out.println(arr[X]);
	}

}
