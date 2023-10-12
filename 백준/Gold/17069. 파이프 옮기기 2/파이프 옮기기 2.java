import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int [][] map = new int[N+1][N+1];
		long [][][] dp = new long[N+1][N+1][3];	// 진행 단계별
		
		// 집 정보
		for(int i = 1; i <= N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j = 1; j <= N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		dp[1][2][0] = 1;	// 초기 위히 가로로 셋팅 -> 1로 초기화
		
		for(int r = 1; r <= N; r++) {
            for(int c = 2; c <= N; c++) {
            	
            	if (r == 1 && c == 2 || map[r][c] == 1) {
					// 초기 위치 or 벽 일때
					continue;
				}
				
            	// 가로 -> 가로, 대각선 
            	dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2];
            	
            	// 세로 -> 세로, 대각선 
            	dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2];

            	if(map[r-1][c] != 1 &&  map[r][c-1] != 1) {
            		dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2];
            	}
				
			}
		}
		 System.out.println(dp[N][N][0] + dp[N][N][1] + dp[N][N][2]);
		
		
	}
}
