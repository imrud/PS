import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**2023-09-25
 * [문제] BJ 145023 : 연구소
 * [아이디어] : 3개의 위치 선택(조합) 후, 그래프 탐색(bfs)진행
 * 1. 3개의 위치 선택(조합)
 * 	(1) 2차원 배열을 1차원 배열로 변환하기 -> 위치값으로 변환
 * 	(2) 변환시킨 값에서 3개를 뽑기
 * 		-> 뽑은 후 2차원 배열에서의 변환값
 * 		-> 현재값을 cur,
 * 		-> 행 : cur/M, 열: cur%M
 * 
 * 2. 위의 변환된 값을 가지고 그래프 탐색 진행(bfs)
 * 	(1) 안전구역은 빈 칸일때, 상하좌우로 진행
 * 	(2) 더이상 진행할 수 없을 경우, 안전지대 변수값을 1 증가하기
 * 
 * 
 * ------
 * [메모리]
 * [실행시간]
 * 
 * @author 허승경
 *
 */
public class Main {
	static int N;
	static int M;
	static int maxArea;		// 안전지대 개수
	static int [][] graph; 
	static int [] dx = {1, 0, -1, 0};	// 사방탐색
	static int [] dy = {0, 1, 0, -1};
	
	// 2. 3개의 벽 세우기
	static void makeWall(int count) {
		if (count == 3) {
			bfs();	// 바이러스 확산
			return;
		}else {
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < M; j++) {
					if(graph[i][j] == 0) {	// 빈 벽일 경우
						graph[i][j] = 1;	// 현재 위치에 벽 세우기
						makeWall(count+1);	// count+1
						graph[i][j] = 0; 	// 현재 위치에 세운 벽 다시 초기화
						
					}
				}
			}
		}
	}
	
	// 3. 바이러스 퍼뜨리기 
	static void bfs() {
		int [][] tmpGraph = new int[N][M];
		
		// graphTmp에 graph 복사(graphTmp에 각 조합마다의 바이러스 분포도 그리고, graph는 계속 원본 유지)
		//tmpGraph = graph.clone();		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				tmpGraph[i][j] = graph[i][j];
			}
		}
		
		
		// bfs 탐색 시작
		Queue<int[]> que = new LinkedList<int[]>();
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(tmpGraph[i][j] == 2) {	// 바이러스일 경우
					que.offer(new int[] {i, j});	// 해당 바이러스의 좌표값
				}
			}
		}
		
		while(!que.isEmpty()) {
			int [] virus = que.poll();
			for(int i = 0; i < 4; i++) {
				
				int nx = virus[0]+dx[i];
				int ny = virus[1]+dy[i];
				
				if(nx >= 0 && nx < N && ny >= 0 && ny < M) {	// 범위조건 만족하고
					if(tmpGraph[nx][ny] == 0) {	// 빈 공간일 때
						tmpGraph[nx][ny] = 2;	// 바이러스 확산
						que.offer(new int[] {nx, ny});
					}
				}
			}
		}
		
		// 한 번의 bfs 다 돌고나서
		int count = 0;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(tmpGraph[i][j] == 0) {	// 빈 공간일 때(= 바이러스 확산 X)
					count++;
				}
			}
		}
		if (count > maxArea) {	// 최대 안전지역 갱신
			maxArea = count;
		}
	}
	
	// 6. 안전지대 구하기
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		// 1. 입력 받기 
		N = Integer.parseInt(st.nextToken());	// 행
		M = Integer.parseInt(st.nextToken());	// 열

		maxArea = 0;
		
		graph = new int[N][M];	// 입력받은 크기만큼 2차원 배열 생성
		
		for(int i = 0; i < N; i++) {	// 그래프 입력받기
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < M; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 2. 벽 세우기
		makeWall(0);

		// 4. 결과 출력
		System.out.println(maxArea);
	}

}
