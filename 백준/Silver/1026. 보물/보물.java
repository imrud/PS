import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());	// 정수 배열의 크기
		
		int [] arrA = new int[N];	// 크기가 N인 배열 A
		int [] arrB = new int[N];	// 크기가 N인 배열 B
		
		// 입력받기
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			arrA[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for(int i = 0 ; i < N; i++) {
			arrB[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arrA);
		Arrays.sort(arrB);
		int sum = 0;
		for(int i = 0; i < N; i++) {
			sum += arrA[i]*arrB[N-i-1];
		}
		
		System.out.println(sum);
		
		
		

	}

}
