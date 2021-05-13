// 프로그래머스_더 맵게

import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < scoville.length; i++) {
            pq.add(scoville[i]);
        }
        
        int cnt = 0;
        while(!pq.isEmpty()) {
            int a = pq.poll();
            if(a >= K) {
                pq.add(a);
                break;
            } else if(pq.isEmpty()){
                break;
            }
            int b = pq.poll();
            int c = a + b * 2;
            pq.add(c);
            cnt++;
        }
        
        if(pq.isEmpty()) {
            answer = -1;
        } else {
            answer = cnt;
        }
        
        return answer;
    }
}