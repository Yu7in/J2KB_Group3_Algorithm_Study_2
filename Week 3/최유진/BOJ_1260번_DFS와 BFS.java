// BOJ_1260번_DFS와 BFS

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static int N, M, V;
	public static ArrayList<ArrayList<Integer>> arr;
	public static ArrayList<Integer> temp;
	public static boolean[] visited;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		StringTokenizer tokens = new StringTokenizer(br.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		V = Integer.parseInt(tokens.nextToken());

		arr = new ArrayList<>();
		for (int i = 0; i <= N; i++) {
			arr.add(new ArrayList<>());
		}

		for (int i = 0; i < M; i++) {
			tokens = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(tokens.nextToken());
			int b = Integer.parseInt(tokens.nextToken());
			arr.get(a).add(b);
			arr.get(b).add(a);
		}

		for (int i = 0; i <= N; i++) {
			Collections.sort(arr.get(i));
		}

		temp = new ArrayList<>();
		visited = new boolean[N + 1];
		dfs(V);
		for (int i = 0; i < temp.size(); i++) {
			sb.append(temp.get(i)).append(" ");
		}
		sb.append("\n");

		temp = new ArrayList<>();
		visited = new boolean[N + 1];
		bfs();
		for (int i = 0; i < temp.size(); i++) {
			sb.append(temp.get(i)).append(" ");
		}
		sb.append("\n");

		System.out.println(sb);
	}

	public static void dfs(int v) {
		temp.add(v);
		visited[v] = true;
		for (int i = 0; i < arr.get(v).size(); i++) {
			if (!visited[arr.get(v).get(i)]) {
				dfs(arr.get(v).get(i));
			}
		}
	}

	public static void bfs() {
		int idx = 0;
		Queue<Integer> q = new LinkedList<>();
		q.add(V);
		while (!q.isEmpty()) {
			int num = q.poll();
			temp.add(num);
			visited[num] = true;
			for (int i = 0; i < arr.get(num).size(); i++) {
				if (!visited[arr.get(num).get(i)]) {
					q.add(arr.get(num).get(i));
					visited[arr.get(num).get(i)] = true;
				}
			}
		}
	}

}
