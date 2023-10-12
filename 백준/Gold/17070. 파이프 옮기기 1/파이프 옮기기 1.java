import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        StringTokenizer st = new StringTokenizer(br.readLine());
	        
	        int N = Integer.parseInt(st.nextToken());
	        
	        int [][] arr = new int[N+1][N+1];			// 집 상태 정보
	        int [][][] dp = new int[N+1][N+1][3];		// 진행 단계별 가로, 세로, 대각선 파이프 개수
	        
	        for(int i = 1; i <= N; i++) {
	            st = new StringTokenizer(br.readLine());
	            for(int j = 1; j <= N; j++) {
	                arr[i][j] = Integer.parseInt(st.nextToken());
	            }
	        }
	        dp[1][2][0] = 1;		// 처음에 가로로 셋팅 -> 1로 초기화
	        // 0 : 가로, 1 : 세로, 2 : 대각선
	        for(int r = 1; r <= N; r++) {
	            for(int c = 2; c <= N; c++) {
	            	
	            	if (r == 1 && c == 2 || arr[r][c] == 1) {
	            		continue;
	            	}
	            	// 가로 -> 가로, 대각선 
	            	dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2];
	            	
	            	// 세로 -> 세로, 대각선 
	            	dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2];

	            	if(arr[r-1][c] != 1 &&  arr[r][c-1] != 1) {
	            		dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2];	            		
	            	}
	            	
	            	// 대각선 -> 가로, 세로, 대각선 
//	            	if(arr[r-1][c] + arr[r][c-1] == 0) {
//						dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2];
//					}

	            }
	        }
	        
	        System.out.println(dp[N][N][0] + dp[N][N][1] + dp[N][N][2]);
		
		
	}

}
