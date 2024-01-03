import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * 2024.01.03
 * 백준 : 2578 빙고
 * 아이디어 : 
 * 1. 부른 숫자 표시하기
 * 2. 숫자가 5개 이상일때부터 가로세로 대각선 판별하기
 * 3. 가로-세로-대각선 합이 3이상이면 해당 숫자 출력
 * 
 * 
 */

public class Main {
	public static void findNum(int n, int [][] arr) {
		for(int i = 0; i < 5; i++) {
			for(int j = 0; j < 5; j++) {
				if(arr[i][j] == n) {
					arr[i][j] = 0;
				}
			}
		}
		
	}
	public static int row(int [][] arr) {
		int count = 0;
		int tmp = 0;
		
		for(int i = 0; i < 5; i++) {
			tmp = 0;
			for(int j = 0; j < 5; j++) {
				tmp += arr[i][j];
			}
			if(tmp == 0) count++;		// 해당 행의 합이 0이면 한 줄 빙고
		}
		return count;
	}
	
	public static int column(int [][] arr) {
		int count = 0;
		int tmp = 0;
		
		for(int i = 0; i < 5; i++) {
			tmp = 0;
			for(int j = 0; j < 5; j++) {
				tmp += arr[j][i];
			}
			if(tmp == 0) count++;		// 해당 열의 합이 0이면 한 줄 빙고
		}
		return count;
	}
	
	public static int rightDiagonal(int [][] arr) {
		int tmp = 0;
		
		for(int i = 0; i < 5; i++) {
			tmp += arr[i][4-i];
		}
		if(tmp == 0) return 1;
		else return 0;
	}
	public static int leftDiagonal(int [][] arr) {
		int tmp = 0;
		
		for(int i = 0; i < 5; i++) {
			tmp += arr[i][i];
		}
		if(tmp == 0) return 1;
		else return 0;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int [][] arr = new int[5][5];		// 빙고 판에 적은 숫자 저장
		StringTokenizer st = null;
		
		for(int i = 0; i < 5; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < 5; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());	// 빙고판에 숫자 저장
			}
		}
		
		int count = 0;	// 철수가 빙고된 숫자의 순서
		int tmp = 0;
		for(int i = 0; i < 5; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < 5; j++) {
				int num = Integer.parseInt(st.nextToken());
				count++;
				findNum(num, arr);	// 부른 숫자는 0으로 표시
				if(count >= 4) {
					// 가로세로 판단
					tmp = row(arr) + column(arr) + rightDiagonal(arr) + leftDiagonal(arr);
					if(tmp >= 3) break;
					tmp = 0;
				}
			}
			if(tmp != 0) break;
		}
		System.out.println(count);
		
		

	}

}
