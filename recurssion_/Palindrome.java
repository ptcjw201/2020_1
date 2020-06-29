package cse2010.homework4;

/*
 * CSE2010 Homework #4
 * Problem 1: Palindrome
 *
 * Complete the code below.
 *
 */

public class Palindrome {

    public static boolean isPalindrome(String target) {

        return isPalindrome(target, 0, target.length() - 1);
    }

    private static boolean isPalindrome(String as, int start, int end) {
    	char c1 = ' '; 
    	char c2 = ' ';
    	while(true) {
    		if(start >= end || start + 2 == end) {
    			return true;
    		}
    		if(!(isAlpha(as.charAt(start)))) {
    			while(isAlpha(as.charAt(start))) {
    				start += 1;
    				if(isAlpha(as.charAt(start))) {
    					c1 = (char) (toLower(as.charAt(start)));
    				}
    			}
    		}
    		if(!(isAlpha(as.charAt(end)))) {
    			while(isAlpha(as.charAt(end))) {
    				end -= 1;
    				if(isAlpha(as.charAt(end))) {
    					c2 = (char) (toLower(as.charAt(end)));
    				}
    			}
    		}
    		if(c1 != c2){
    			break;
    		}start += 1; end -= 1;
    	}
        return false;
    }

    private static boolean isAlpha(final char ch) {
        if (ch >= 'a' && ch <= 'z' || ch >= 'A' && ch <= 'Z')
            return true;
        else
            return false;
    }

    private static int toLower(char c) {
        if ((c >= 'A') && (c <= 'Z'))
            return c + ('a' - 'A');
        return c;
    }

}
