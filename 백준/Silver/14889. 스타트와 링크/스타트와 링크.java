import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
	static int n;
	static int[][] arr;
	static int[] start; // start 조합 담는 배열
	static int[] end; // end 조합 담는 배열
	static int minAbility;

	public static void comb(int count, int idx) {
		if (count == n/2) {
			// 조합 생성 완료
			findComb();
//			System.out.println("start : "+Arrays.toString(start));
//			System.out.println("end : "+Arrays.toString(end));

			sumPower();
			return;
		}

		for (int i = idx; i < n; i++) {
			start[count] = i + 1;
			comb(count + 1, i + 1);
		}

	}

	public static void findComb() {
		// 남은 조합 구하기
		int[] nums = new int[n + 1];

		for (int i = 0; i < start.length; i++) {
			nums[start[i]] = 1;
		}
		
		int count = 0;
		for (int i = 1; i < nums.length; i++) {
			if (nums[i] != 1) {
				end[count++] = i;
			}
		}
		
		return;
	}

	public static void sumPower() {
		// (1) start 팀 능력치 구하기
		int sumStart = 0;
		for (int i = 0; i < start.length; i++) {
			for (int j = 0; j < start.length; j++) {
				if (i != j) {
					sumStart += arr[start[i]-1][start[j]-1];
				}
			}
		}

		// (1) end 팀 능력치 구하기
		int sumEnd = 0;
		for (int i = 0; i < end.length; i++) {
			for (int j = 0; j < end.length; j++) {
				if (i != j) {
					sumEnd += arr[end[i]-1][end[j]-1];
				}
			}
		}
//		System.out.println(sumStart + " : "+sumEnd+ " : "+ Math.abs(sumStart-sumEnd));
		// 최소값 구하기
		minAbility = Math.min(minAbility, Math.abs(sumStart-sumEnd));
		
		return;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		n = Integer.parseInt(br.readLine());

		arr = new int[n][n]; // 능력치 입력받기
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 1. 스타트와 링크를 나누는 조합 구하기
		start = new int[n / 2];
		end = new int[n / 2];
		minAbility = Integer.MAX_VALUE;
		comb(0, 0);
		
		System.out.println(minAbility);

	}

}
