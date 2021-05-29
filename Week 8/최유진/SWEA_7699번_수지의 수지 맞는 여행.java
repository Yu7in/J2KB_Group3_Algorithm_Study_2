//SWEA_7699번_수지의 수지 맞는 여행

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class Solution {
 
    public static int R, C, ans;
    public static char[][] arr;
    public static boolean[] visited;
    public static int[][] dirs = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
 
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer tokens = new StringTokenizer(br.readLine());
            R = Integer.parseInt(tokens.nextToken());
            C = Integer.parseInt(tokens.nextToken());
 
            arr = new char[R][C];
            for (int i = 0; i < R; i++) {
                String str = br.readLine();
                for (int j = 0; j < C; j++) {
                    arr[i][j] = str.charAt(j);
                }
            }
 
            ans = 0;
            visited = new boolean['Z' - '0' + 1];
            dfs(0, 0, 1);
 
            sb.append("#").append(tc).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }
 
    public static void dfs(int x, int y, int cnt) {
        visited[arr[x][y] - '0'] = true;
        for (int i = 0; i < dirs.length; i++) {
            int dx = x + dirs[i][0];
            int dy = y + dirs[i][1];
            if (dx >= 0 && dy >= 0 && dx < R && dy < C) {
                if (!visited[arr[dx][dy] - '0']) {
                    dfs(dx, dy, cnt + 1);
                }
            }
        }
        ans = ans < cnt ? cnt : ans;
        visited[arr[x][y] - '0'] = false;
    }
 
}