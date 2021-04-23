//
//  main.c
//  backjune_1012
//
//  Created by 장두혁 on 2021/04/24.
//

#include <stdio.h>

#define row 50
#define col 50
int dy[] = {-1, 1,0,0};
int dx[] = {0,0,-1, 1};
int ans = 0;

void location_baechu(int a[row][col]){
    int row_case,col_case =0;
    scanf("%d %d",&row_case,&col_case);
    a[row_case][col_case] = 1;
}

void dfs(int v[row][col],int a[row][col],int i,int j){
    v[j][i] = 1;
    for (int k=0; k<4; k++) {
        int ny = j + dy[k];
        int nx = i + dx[k];
        if ( ny < 0 || nx < 0 || ny>= row || nx >=col) continue;
        if(a[ny][nx] == 1 && !v[ny][nx] )
            dfs(v,a,ny,nx);
    }
}

void agriculturing(int v[row][col],int a[row][col],int *row_count,int *col_count){
    int at_once = 0;
    scanf("%d %d %d",row_count,col_count,&at_once);
    for (int i = 0; i < at_once;i++) {
        location_baechu(a);
    }
    
    for (int i=0 ; i<row_count; i++) {
        for (int j=0; j<col_count; j++) {
            dfs(v, a,i,j);
            ans++;
        }
    }
}



void print_field(int a[row][col],int *row_real,int *col_real){
    printf("%d %d\n",*row_real,*col_real);
    for (int i = 0; i < *row_real; i++) {
        for (int j=0; j < *col_real; j++) {
            printf("%2d",a[i][j]);
        }
        printf("\n");
    }printf("\n");
}




int main(int argc, const char * argv[]) {
    int row_real = 0;
    int col_real =0;
    int *row_p;
    int *col_p;
    row_p=&row_real;
    col_p=&col_real;
    
    int time =0;
    scanf("%d",&time);
    
    for (int i =0; i<time; i++) {
        int field[row][col] = { 0,};
        int visited[row][col] = { 0,};
        agriculturing(visited,field,row_p,col_p);

        print_field(field,row_p,col_p);
        printf("count : %2d\n",ans);
        ans = 0;
        
    }
    return 0;
}
