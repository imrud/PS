import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/*
 * 2024-01-02
 * 백준 : 20291 파일정리
 * 아이디어 : 
 * 1. (확장자, 개수)형식의 리스트로 저장
 * 2. 확장자를 사전순으로 정렬해서 출력
 * -> 시간초과
 * 
 * map을 이용해서 해결
 * 
 */
public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());	// 파일 개수
		
		Map<String, Integer> map = new TreeMap<>();
		
		for(int i = 0; i < n; i++) {
			String tmp = br.readLine().split("\\.")[1];
			if(map.containsKey(tmp)) {	// 이미 존재하는 확장자인경우
				int cnt = map.get(tmp);
				map.replace(tmp, ++cnt);
			}
			else {
				map.put(tmp, 1);
			}
		}
		
		for(String key : map.keySet()) {
			System.out.println(key+" "+map.get(key));
		}
	}
}



//class FileInfo{
//	private String extension;
//	private int count;
//	
//	public FileInfo(String extension, int count) {
//		this.extension = extension;
//		this.count = count;
//	}
//	
//	public void setExtension(String extension) {
//		this.extension = extension;
//	}
//	public String getExtension() {
//		return extension;
//	}
//	public void setCount(int count) {
//		this.count = count;
//	}
//	public int getCount() {
//		return count;
//	}
//
//}
//
//class ListComparator implements Comparator<FileInfo>{
//	
//	public int compare(FileInfo o1, FileInfo o2) {
//		
//		String ex1 = ((FileInfo)o1).getExtension();
//		String ex2 = ((FileInfo)o2).getExtension();
//		
//		return (o1.getExtension()).compareTo(o2.getExtension());
//	}
//}
//
//public class BJ_20291_파일정리 {
//	
//
//	public static void main(String[] args) throws NumberFormatException, IOException {
//		// TODO Auto-generated method stub
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		int n = Integer.parseInt(br.readLine());	// 파일 개수
//		
//		List<FileInfo> list = new ArrayList<FileInfo>();	// 분리한 확장자, 확장자 수를 담을 리스트 생성
//		boolean flag = false;
//		
//		for(int i = 0; i < n; i++) {
//			String str = br.readLine();
//			String tmp = str.split("\\.")[1];	// '.' 기준으로 문자열 분리
//
//			for(int j = 0; j < list.size(); j++) {
//				if(list.get(j).getExtension().equals(tmp)) {	// 이미 확장자가 존재하는 경우
//					int update = list.get(j).getCount() + 1;	// 1증가
//					list.get(j).setCount(update);	
//					flag = true;
//				}
//			}
//
//			if(!flag) { // 존재하지 않은 경우 -> 해당 확장자와 개수를 삽입
//				FileInfo info = new FileInfo(tmp, 1);	// 확장자, 1
//				list.add(info);
//				
//			}
//			flag = false;
//		}
//		
//		
//		Collections.sort(list, new ListComparator()); 		// 오름차순 정렬
//		
//		
//		for(FileInfo info : list) {
//			System.out.println(info.getExtension()+" "+info.getCount());
//		}
//		
//		
//		
//		
//		
//		
//
//	}
//
//}
