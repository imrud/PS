import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**2023-10-05
 * [문제] SWEA 5656 : 벽돌 깨기
 * [아이디어]
 *  1. 구슬 떨어뜨리기
 *  	- N번 동안 떨어질 열 구하기
 *  	- 중복 순열 사용
 *  		-> 같은위치에 다시 떨어뜨려도 O
 *  		-> 떨어뜨리는 열의 순서에 따라 결과값이 달라짐 = 순서에 가치가 부여됨
 *  
 *  2. 벽돌 깨기
 *  	- 그래프 탐색
 *  	- 이때, 깨는 구슬만큼 영향력 있음!
 *  3. 깨는 과정에서 빈공간이 있으면 아래로 떨어짐
 *  4. 최종적으로 남은 벽돌 개수 구하기
 *  5. 위의 과정을 반복하면서 남은 벽돌의 개수가 최소인 경우를 갱신한다.
 * 
 * [메모리]
 * [실행시간]
 * 
 * 
 * @author 허승경
 *
 */
public class Solution {
	static int N, W, H;
	static int [][] map;
	static int [][] tmpMap;
	static int [] turns;	// 구슬을 떨어뜨리는 순서
	static int tmpCount = 0;	// 각 케이스마다 제거할 수있는 벽돌
	
	static int [] dx = {0, -1, 0, 1};	// 사방탐색
	static int [] dy = {-1, 0, 1, 0};
	static int maxBrick;	// 부순 벽돌의 최댓값
	
	private static void permutation(int count){
		// 중복 순열 -> 구슬을 떨어뜨릴 열 선택
		if(count == N) {
			// N개의 중복 순열 생성 완료
			// 2. 구한 순열대로 구슬 떨어뜨리기
			dropBead();
			return;
		}
		
		for(int i = 0; i < W; i++) {
			turns[count] = i;
			permutation(count+1);
		}
	}
	
	private static void dropBead() {
		// 복사한 전체벽돌 배열로 각 케이스 실행하기
		tmpMap = new int[H][W];
		for(int i = 0; i < H; i++) {
			tmpMap[i] = map[i].clone();
		}
		
		tmpCount = 0;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < H; j++) {
				// 선정 된 순열 위치 중 가장 맨 위에 있는 벽돌부터 깨기 
				if(tmpMap[j][turns[i]] != 0) {
					// 3. 벽돌 부시기
					breakBrick(j, turns[i]);
					break;	// 현재 반복문 벗어나기(현재 순열의 진행 끝났으니 다음으로 넘어가기위해)
				}
			}
			
			// 4. 떠 있는 벽돌 제거
			dropBrick();			
		}
		
		// 5. 더 많은 벽돌을 부순 경우 = 남은 벽돌의 개수가 최소일 때를 갱신
		maxBrick = Math.max(maxBrick, tmpCount);
	}

	private static void dropBrick() {
		for(int i = H-2; i >= 0; i--) {
			// 가장 밑 행부터 확인하기
			for(int j = 0; j < W; j++) {
				// 현재 위치는 빈칸 + 그 아래는 비어 있을 경우
				if(tmpMap[i][j] != 0 && tmpMap[i+1][j] == 0) {
					int x = i;
					for(int k = i+1; k < H; k++) {
						// 다른 벽돌 만나기 전까지 하강
						if(tmpMap[k][j] != 0) {	
							break;
						}
						x = k;	// 그때의 위치 저장
					}
					tmpMap[x][j] = tmpMap[i][j];	// 벽돌 위치 수정하기
					tmpMap[i][j] = 0;
				}
			}
		}
		
	}

	private static void breakBrick(int x, int y) {
		int range = tmpMap[x][y] - 1;	// 벽돌의 깨뜨리는 범위
		
		tmpCount++;	// 먼저 타겟 벽돌 개수 증가
		tmpMap[x][y] = 0;	// 해당 위치 벽돌 없애주기
		
		// 주위 벽돌깨기
		for(int i = 0; i < 4 ;i++) {
			// 사방으로, 폭발 범위만큼 영향력 행사
			for(int j = 1; j <= range; j++) {
				
				int nx = x + dx[i] * j;
				int ny = y + dy[i] * j;
				
				// 범위내에 존재 + 해당 위치가 벽돌
				if(nx >= 0 && nx < H && ny >= 0 && ny < W && tmpMap[nx][ny] != 0) {
					// 깨진 위치에서의 폭발 진행
					breakBrick(nx, ny);
				}
			}
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for(int t = 1; t <= T; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			H = Integer.parseInt(st.nextToken());
			
			map = new int[H][W];
			turns = new int[N];
			maxBrick = Integer.MIN_VALUE;
			
			// 초기 벽돌 정보 입력받기
			int totalBrick = 0;
			for(int i = 0; i < H; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j < W; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if(map[i][j] != 0) {
						totalBrick++;
					}
				}
			}
			
			// 1. 중복순열 -> 구슬을 떨어뜨릴 위치 선정
			permutation(0);	
			// 케이스마다 결과
			sb.append("#"+t+" "+(totalBrick-maxBrick)+"\n");
			
		}
		System.out.println(sb);
	}
}
