//SWEA_1767번_프로세서 연결하기

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
 
public class Solution {
    public static int N, ans, maxNum;
    public static int[][] arr;
    public static ArrayList<int[]> core;
    public static int[][] dirs = { { 0, -1 }, { -1, 0 }, { 0, 1 }, { 1, 0 } };
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
 
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
 
            arr = new int[N][N];
            core = new ArrayList<int[]>();
            for (int i = 0; i < N; i++) {
                StringTokenizer tokens = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(tokens.nextToken());
                    if (arr[i][j] == 1) {
                        core.add(new int[] { i, j });
                    }
                }
            }
 
            ans = Integer.MAX_VALUE;
            maxNum = 0;
            minLen(0, 0, 0);
 
            sb.append("#").append(tc).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }
 
    public static void minLen(int c, int sum, int num) {
        if (c == core.size()) {
            if (maxNum == num) {
                ans = ans > sum ? sum : ans;
            } else if (maxNum < num) {
                maxNum = num;
                ans = sum;
            }
            return;
        }
 
        int x = core.get(c)[0];
        int y = core.get(c)[1];
        if (x == 0 || y == 0 || x == N - 1 || y == N - 1) {
            minLen(c + 1, sum, num + 1);
        } else {
            for (int i = 0; i < dirs.length; i++) {
                int cnt = 1;
                while (true) {
                    int dx = x + dirs[i][0] * cnt;
                    int dy = y + dirs[i][1] * cnt;
                    if (dx >= 0 && dy >= 0 && dx < N && dy < N) {
                        if (arr[dx][dy] == 0) {
                            cnt++;
                        } else {
                            cnt = 1;
                            break;
                        }
                    } else {
                        break;
                    }
                }
                if (cnt != 1) {
                    for (int k = 1; k < cnt; k++) {
                        arr[x + dirs[i][0] * k][y + dirs[i][1] * k] = 1;
                    }
 
                }
                if (cnt != 1)
                    minLen(c + 1, sum + cnt - 1, num + 1);
                else
                    minLen(c + 1, sum + cnt - 1, num);
                if (cnt != 1) {
                    for (int k = 1; k < cnt; k++) {
                        arr[x + dirs[i][0] * k][y + dirs[i][1] * k] = 0;
                    }
                }
            }
        }
    }
}