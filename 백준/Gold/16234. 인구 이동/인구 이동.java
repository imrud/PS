import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;


public class Main {
	static int N;
	static int L;
	static int R;
	static int[][] arr;
	static boolean[][] visited;
	static int [] dx = {-1, 0, 1, 0};
	static int [] dy = {0, -1, 0, 1};
	
	public static void bfs(int x, int y) {
		List<int []> list = new LinkedList<int[]>();	// 현재 위치와 연결된 나라의 위치 담는 리스트
		list.add(new int[] {x, y});	// 현재 위치 담기
		
		Queue<int[]> que = new LinkedList<int[]>();
		que.offer(new int[] {x, y});
		visited[x][y] = true;	// 현재 위치 방문 확인 처리
		
		int population = arr[x][y];	// 연합인 나라의 전체 인구수
		int count = 1;	// 현재 연합인 나라 수((x,y) 하나 존재)
		
		int nx = 0;
		int ny = 0;
		while(!que.isEmpty()) {
			int [] tmp = que.poll();
			x = tmp[0];
			y = tmp[1];
			for(int i = 0; i < 4; i++) {
				nx = x + dx[i];
				ny = y + dy[i];
				
				// 범위 내에 위치  + 아직 방문 전
				if(nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
					// (x, y)와 (nx, ny)의 인구수 차이가 조건 안에 들 경우
					if(L <= (Math.abs(arr[x][y] - arr[nx][ny])) 
							&& (Math.abs(arr[x][y] - arr[nx][ny])) <= R) {
						que.add(new int[] {nx, ny});
						visited[nx][ny] = true;	// 방문확인
						population += arr[nx][ny];	// 연합인 나라의 인구수 증가
						count++;
						list.add(new int[] {nx, ny});
					}
				}
			}
		}
		
		// 인구수 분배하기
		for(int i = 0; i < list.size(); i++) {
			int [] tmp = list.get(i);
			arr[tmp[0]][tmp[1]] = population/count;	// 인구수 분배
		}
		
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());

		arr = new int[N][N]; // 입력받은 크기만큼 2차원 인구 배열 생성

		for (int i = 0; i < N; i++) { // 인구 입력받기
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int result = 0;
		while (true) {
			visited = new boolean[N][N]; // 방문확인 배열
			int count = 0; // 인구 이동 횟수

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (!visited[i][j]) {
						// 아직 방문전일때 bfs 돌리기
						bfs(i, j);
						count++;
					}
				}
			}
			if (count == N * N) { // 모든 인구 탐색 완료
				break;
			}
			result++;

		}
		System.out.println(result);
		
		
		
	}

}
