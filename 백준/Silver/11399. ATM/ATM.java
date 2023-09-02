import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int [] arr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		// step1.정렬
		Arrays.sort(arr);
		
		// step2. 누적합 구하기
		for(int i = 1; i <N; i++) {
			arr[i] = arr[i]+arr[i-1];
		}
		
		// step3. 시간 합의 최솟값 출력
		int minTime = 0;
		for(int i = 0; i < N; i++) {
			minTime += arr[i];
		}
		
		System.out.println(minTime);

	}

}
