import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int[][] room;
    static Set<Integer>[] like;
    static int N, ans;

    @SuppressWarnings("unchecked")
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        room = new int[N+2][N+2];
        like = (Set<Integer>[]) new HashSet[N*N+1];
        for (int i = 1; i <= N*N; i++) {
            like[i] = new HashSet<Integer>();
        }
        for (int i = 0; i < N*N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            for (int j = 0; j < 4; j++) {
                like[num].add(Integer.parseInt(st.nextToken()));
            }
            place(num);
        }
        calc();
        System.out.println(ans);
    }


    static void place(int num) {
        Favorite f = new Favorite(0, 0, N+1, N+1); // 최솟값
        for (int r = 1; r <= N; r++) {
            for (int c = 1; c <= N; c++) {
                if (room[r][c] != 0) continue;
                int likeNum = 0;
                int emptyNum = 0;
                for (int i = 0; i < 4; i++) {
                    int nr = r + dr[i], nc = c + dc[i];
                    if (nr < 1 || nr > N || nc < 1 || nc > N) continue;
                    if (room[nr][nc] == 0) emptyNum++;
                    if (like[num].contains(room[nr][nc])) likeNum++;
                }
                Favorite temp = new Favorite(likeNum, emptyNum, r, c);
                if (f.compareTo(temp) < 0) {
                    f = temp;
                }
            }
        }
        room[f.row][f.col] = num;
    }


    static void calc() {
        int[] satis = {0, 1, 10, 100, 1000};
        for (int r = 1; r <= N; r++) {
            for (int c = 1; c <= N; c++) {
                int cnt = 0;
                for (int i = 0; i < 4; i++) {
                    int nr = r + dr[i], nc = c + dc[i];
                    if (like[room[r][c]].contains(room[nr][nc])) cnt++;
                }
                ans += satis[cnt];
            }
        }
    }

    static class Favorite implements Comparable<Favorite>{
        int like;
        int empty;
        int row;
        int col;

        public Favorite(int like, int empty, int row, int col) {
            super();
            this.like = like;
            this.empty = empty;
            this.row = row;
            this.col = col;
        }

        @Override
        public int compareTo(Favorite o) {
            if (this.like == o.like) {
                if (this.empty == o.empty) {
                    if (this.row == o.row) {
                        return - (this.col - o.col);
                    }
                    return - (this.row - o.row);
                }
                return this.empty - o.empty;
            }
            return this.like - o.like;
        }
    }
}