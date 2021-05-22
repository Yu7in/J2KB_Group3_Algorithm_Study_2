//프로그래머스_프렌즈4블록

import java.util.*;

class Solution {
    public int solution(int m, int n, String[] board) {
        int answer = 0;
        
        char[][] arr = new char[m][n];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                arr[i][j] = board[i].charAt(j);
            }
        }
        
        int cnt = 0;
        HashSet<Node> hs = new HashSet<>();
        while(true) {
            for(int i = 0; i < m - 1; i++) {
                for(int j = 0; j < n - 1; j++) {
                    char ch = arr[i][j];
                    if(ch == 'X')
                    	continue;
                    
                    if(ch == arr[i][j+1] && ch == arr[i+1][j] && ch == arr[i+1][j+1]) {
                        hs.add(new Node(i, j));
                        hs.add(new Node(i+1, j));
                        hs.add(new Node(i, j+1));
                        hs.add(new Node(i+1, j+1));
                    }
                }
            }
            
            if(hs.size() == 0) {
                break;
            }
            
            Iterator iter = hs.iterator();
            while(iter.hasNext()) {
                Node node = (Node) iter.next();
                if(arr[node.x][node.y] != 'X') {
                    arr[node.x][node.y] = 'X';
                    cnt++;
                }
            }
            
            for(int i = 0; i < m; i++) {
                for(int j = 0; j < n; j++) {
                    if(arr[i][j] == 'X') {
                        for(int k = i-1; k >= 0; k--) {
                            arr[k+1][j] = arr[k][j];
                        }
                        arr[0][j] = 'X';
                    }
                }
            }
            hs.clear();
        }
        
        answer = cnt;
        
        return answer;
    }
    
    public static class Node{
        int x;
        int y;
        public Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}