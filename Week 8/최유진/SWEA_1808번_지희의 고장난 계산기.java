//SWEA_1808번_지희의 고장난 계산기

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
 
public class Solution {
 
    public static int X;
    public static int[] checked;
    public static ArrayList<Integer> number;
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
 
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            checked = new int[10];
            StringTokenizer tokens = new StringTokenizer(br.readLine());
            for (int i = 0; i < 10; i++) {
                checked[i] = Integer.parseInt(tokens.nextToken());
            }
 
            X = Integer.parseInt(br.readLine());
 
            int len = 0;
            int temp = X;
            while (temp > 0) {
                temp /= 10;
                len++;
            }
 
            number = new ArrayList<>();
            for (int i = 1; i <= len; i++) {
                makeNum(0, i, new int[i]);
            }
 
            int ans = findNum(X) == Integer.MAX_VALUE ? -1 : findNum(X);
            sb.append("#").append(tc).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }
 
    public static void makeNum(int n, int N, int[] temp) {
        if (n == N) {
            String str = "";
            for (int i = 0; i < temp.length; i++) {
                str += temp[i];
            }
//          if (!number.contains(Integer.parseInt(str))) {
//              number.add(Integer.parseInt(str));
//          }
            number.add(Integer.parseInt(str));
        } else {
            for (int i = 0; i < 10; i++) {
                if (checked[i] == 1) {
                    temp[n] = i;
                    makeNum(n + 1, N, temp);
                }
            }
        }
    }
 
    public static int findNum(int num) {
//      if (num == 1)
//          return 0;
        if (number.contains(num)) {
            int len = 0;
            while (num > 0) {
                num /= 10;
                len++;
            }
            return len + 1;
        }
 
        int minn = Integer.MAX_VALUE;
        for (int i = 0; i < number.size(); i++) {
            if (number.get(i) > num)
                break;
            if (number.get(i) > 1 && num % number.get(i) == 0) {
                int len = 0;
                int temp = number.get(i);
                while (temp > 0) {
                    temp /= 10;
                    len++;
                }
                int N = findNum(num / number.get(i));
                if (N == Integer.MAX_VALUE)
                    continue;
                temp = len + N + 1;
                minn = minn > temp ? temp : minn;
            }
        }
 
        return minn;
    }
 
}