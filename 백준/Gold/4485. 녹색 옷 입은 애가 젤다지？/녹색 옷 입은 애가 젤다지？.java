import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] map;
	static int[] dx = { 0, -1, 0, 1 }; // 사방탐색
	static int[] dy = { -1, 0, 1, 0 };

	private static void bfs(int i, int j) {

		PriorityQueue<int[]> que = new PriorityQueue<>(new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[0] == o2[0]) {
					if (o1[1] == o2[1]) {
						// 도둑루피, 행이 같다면 열 기준 오름차순 정렬
						return Integer.compare(o1[2], o2[2]);
					}
					// 도둑루피가 같다면 행 기준 오름차순 정렬
					return Integer.compare(o1[1], o2[1]);
				}

				// 도둑루피가 더 작은 값을 기준으로 오름차순 정렬
				return Integer.compare(o1[0], o2[0]);
			}
		});

//		Queue<int []> que = new LinkedList<int []>();
		boolean[][] visited = new boolean[N][N];
		visited[i][j] = true;

		que.offer(new int[] { map[i][j], i, j }); // 현재 위치의 도둑루피, 현재 위치 행, 열

		int nx = 0;
		int ny = 0;
		int k = 0;
		while (!que.isEmpty()) {
			int[] cur = que.poll();

			for (int idx = 0; idx < 4; idx++) {
				k = cur[0];
				nx = cur[1] + dx[idx];
				ny = cur[2] + dy[idx];

				// 범위 내에 위치 + 아직 방문전
				if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {

					visited[nx][ny] = true;
					map[nx][ny] += k; // 이전 값과 더해주기
					que.offer(new int[] { map[nx][ny], nx, ny });
				}
			}
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		StringBuilder sb = new StringBuilder();

		int count = 1;
		while (true) {
			N = Integer.parseInt(br.readLine()); // 동굴의 크기

			if (N == 0)
				break; // 0 입력 시 반복문 종료
			
			map = new int[N][N];
			// 도둑루피 입력받기
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			// 1. 동굴의 제일 왼쪽에서 출발(0, 0)
			bfs(0, 0);
			sb.append("Problem " + count++ + ": " + map[N - 1][N - 1] + "\n");

		}

		System.out.println(sb);

	}

}
