import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	
	static int n;
	static int m;
	static int [][] graph;
	static boolean [][] visited;
	static int [] dx = {-1, 1, 0, 0};		// 상-하-좌-우
	static int [] dy = {0, 0, -1, 1};
	static int count;
	static int tmpArea;
	
	static void dfs(int x, int y) {
		visited[x][y] = true;		// 방문 확인
		tmpArea++;	// 해당 그림의 넓이
		
		int nx = 0;
		int ny = 0;
		for(int i = 0; i < 4; i++) {
			nx = x + dx[i];
			ny = y + dy[i];

			// 범위 벗어나거나 이미 방문했다면 다음 차례로
			if(nx >= 0 && nx < n && ny >= 0 && ny < m) {
				if(!visited[nx][ny] && graph[nx][ny] == 1) {
					dfs(nx, ny);
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());	// 세로 크기(행)
		m = Integer.parseInt(st.nextToken());	// 가로 크기(열)
		
		graph = new int[n][m];		// 그림 정보 배열
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// dfs 돌리기
		count = 0;	// 그림의 개수
		int maxArea = 0;	// 가장 넓은 그림의 넓이
		visited = new boolean[n][m];	// n*m 크기의 방문 배열
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				tmpArea = 0;
				if(graph[i][j] == 1 && !visited[i][j]) {	// 그림이고 아직 방문 전
					dfs(i, j);
					count++;
					maxArea = Math.max(maxArea, tmpArea);
				}
			}
		}
		System.out.println(count+"\n"+maxArea); 	// 결과 출력
		
		
		
		
		

	}

}
