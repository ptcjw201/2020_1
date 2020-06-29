package cse2010.homework4;

/*
 * CSE2010 Homework #4
 * Problem 2: Fibonacci (Tail-Recursion)
 *
 * Complete the code below.
 *
 */

public class Fibonacci {

    public static int fib(int n) {
        if (n == 0 || n == 1)
            return n;
        else
            return fib(n - 2) + fib(n - 1);
    }

    public static int fibIter(int n) {
        if (n <= 1)
            return n;

        int acc = 1;
        int prev = 0;

        while (n-- > 1) {
            int temp = acc;
            acc += prev;
            prev = temp;
        }

        return acc;
    }

    private static int fibcall(int n, int start, int end) {
    	if(n == 0) {
    		System.out.println(start);
    		return start;
    	}
    	else{
    		return fibcall(n-1, end, start + end);
    	}
    }
    
    public static int fibTailRec(int n) {
    	if(n > 0) {
    		return fibcall(n,0,1);
    	}
    	return 0;
    }


}
