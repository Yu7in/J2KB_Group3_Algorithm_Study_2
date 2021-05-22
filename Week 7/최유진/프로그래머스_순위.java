//프로그래머스_순위

import java.util.*;

class Solution {
    public static ArrayList<HashSet<Integer>> up;
    public static ArrayList<HashSet<Integer>> down;
    
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        up = new ArrayList<>();
        down = new ArrayList<>();
        
        for(int i = 0; i <= n; i++) {
            up.add(new HashSet<>());
            down.add(new HashSet<>());
        }
        
        for(int i = 0; i < results.length; i++) {
            up.get(results[i][1]).add(results[i][0]);
            down.get(results[i][0]).add(results[i][1]);
        }
        
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                if(i == j)
                    continue;
                
                if(up.get(j).contains(i)) {
                    for (Integer num : up.get(i)) {
                        up.get(j).add(num);
                    }
                }
                
                if(down.get(j).contains(i)) {
                    for (Integer num : down.get(i)) {
                        down.get(j).add(num);
                    }
                }
            }
        }
        
        for(int i = 1; i <= n; i++) {
            int cnt = up.get(i).size() + down.get(i).size();
            if(cnt == n-1)
                answer++;
        }
        
        return answer;
    }
}