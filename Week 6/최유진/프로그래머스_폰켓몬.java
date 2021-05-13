// 프로그래머스_폰켓몬

import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        HashSet<Integer> hs = new HashSet<>();
        for(int i = 0; i < nums.length; i++)
            hs.add(nums[i]);
        
        int cnt = hs.size();
        answer = cnt <= nums.length/2 ? cnt : nums.length/2;
        
        return answer;
    }
}