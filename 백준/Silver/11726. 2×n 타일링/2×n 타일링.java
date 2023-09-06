import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int [] dp = new int[n+1];
		
		// 미리 초기화 시키려면 dp의 크기를 먼저 지정하기
		if(n==1) {
			System.out.println(1);
		}else if(n==2) {
			System.out.println(2);
		}else {
			dp[1] = 1;
			dp[2] = 2;
			for(int i = 3; i <= n; i++) {
				dp[i] = (dp[i-1] + dp[i-2]) % 10007;
			}
			System.out.println(dp[n]);			
		}
	}

}
