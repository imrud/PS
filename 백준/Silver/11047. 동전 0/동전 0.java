import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int [] arr = new int[N];
		
		// 큰 값부터 나누기 위해(나중에 정렬 안 돌릴려고)
		for(int i = N-1; i >= 0; i--) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		int count = 0;		// K원을 만드는데 필요한 동전 개수의 최솟값
		int tmp = K;

		for(int i = 0; i < N; i++) {
			if(K/arr[i] > 0) {			// 나눌 수 있다면, 몫은 동전 개수에 추가, K값은 나머지로 갱신
				count += K/arr[i];
				K %= arr[i];
			}
		}
		
		System.out.println(count);
	}

}
