import java.util.Scanner;
import java.util.Stack;

class Main {
    public static int solution(String s) {
        Stack<Character> stack = new Stack<>();
        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push('(');
            } else {
               stack.pop();
               if(s.charAt(i - 1) == '(') {
                   answer += stack.size();
               } else {
                   answer++;
               }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        System.out.println(solution(s));
    }
}