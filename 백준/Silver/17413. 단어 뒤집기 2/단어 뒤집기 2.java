import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
 * 2024_01_01
 * 백준 : 단어 뒤집기2
 * 
 */
public class Main {
	public static String reverse(String word) {
		String rWord = "";
		for(int i = word.length()-1; i >= 0; i--) {
			rWord += word.charAt(i);
		}
		
		return rWord;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String original_str = br.readLine();	// 문자열 S 입력받기
		String result = "";
		boolean flag = false;
		String word = "";
		
		for(int i = 0; i < original_str.length(); i++) {
			if(original_str.charAt(i) == '<') {
				if(word.length() > 0) {
					result += reverse(word);
					word = "";		
				}
				result += original_str.charAt(i);
				
				flag = true;
				word = "";
			}
			else if(original_str.charAt(i) == '>') {
				result += original_str.charAt(i);
				if(word.length() > 0) {
					result += reverse(word);
					word = "";		
				}
				flag = false;
			}
			else if(original_str.charAt(i) == ' ') {
				if(word.length() > 0) {
					result += reverse(word);
					word = "";					
				}
				result += " ";
			}
			else if(Character.isLowerCase(original_str.charAt(i)) || Character.isDigit(original_str.charAt(i))){
				if(flag) {
					result += original_str.charAt(i);
				}else {
					word += original_str.charAt(i);
				}
			}
		}
		if(word != "") {
			result += reverse(word);
		}
		System.out.println(result);
		
		
	}

}
