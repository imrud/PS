import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int [] numbers;		// 순열 담을 배열
	static boolean [] visited;	// 순열 생성시 방문 배열
	static int [][] arr;
	static int min;
	
	// 순열 생성 메소드
	static void permutation(int count) {
		if(count == N) {
			
			// step 3: 현재 만들어진 순열로 최소 비용 구하기
			minCost();
			
			return;
		}
		
		for(int i = 0; i < N; i++) {
			if(!visited[i]) {			// 방문 전
				visited[i] = true;		// 방문 처리
				numbers[count] = i;		// 순열 값 생성
				permutation(count+1);	// count 1증가한 채로 가기
				visited[i] = false;		// i에 대한 방문 처리 취소
			}
		}
	}
	
	// 최소 비용 구하는 메소드
	static void minCost() {
		
		// step 2: 각 순열의 인접여부 확인하러 가기
		if(checkAdj()) {	// 인접 확인 조건 만족
			int tmpSum = 0;
			
			for(int i = 0; i < numbers.length-1; i++) {
				tmpSum += arr[numbers[i]][numbers[i+1]];	// i -> i+1 가는 비용
				
			}
			tmpSum += arr[numbers[N-1]][numbers[0]];	// N번째에서 첫 번째 집으로 가는 비용
			min = Math.min(min, tmpSum);
		}
	}
	
	// 인접 확인하는 메소드
    static boolean checkAdj() {
    	
		// part1 : 마지막 집과 첫 번째 집의 인접 여부 
    	if(arr[numbers[N-1]][numbers[0]] == 0) {	// 서로의 가중치가 없음 -> 연결 안 된 상태 -> 해당 배열은 실패
    		return false;
    	}
    	
    	// part2 : 순열대로의 인접 여부
    	for(int i = 0; i < numbers.length-1; i++) {
    		if(arr[numbers[i]][numbers[i+1]] == 0) {	// 서로 인접하지 않다면
    			return false;
    		}
    	}
    	
    	return true;
		
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= null;
        
        N = Integer.parseInt(br.readLine());
        
        arr = new int[N][N];
        
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        // step 1: 순열 만들기
        numbers = new int[N];		// 순열 저장할 배열
        visited = new boolean[N];	// 방문 처리할 배열
        min = Integer.MAX_VALUE;
        permutation(0);
        
        System.out.println(min);

    }

}