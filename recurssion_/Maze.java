package cse2010.homework4;
/*
 * CSE2010 Homework #4:
 * Problem 3: Maze
 *
 * Complete the code below.
 */

import java.util.Arrays;

import cse2010.homework4.Location;

public class Maze {
    private int numRows;
    private int numCols;

    private int[][] maze;
    private boolean[][] visited = null;

    private Location entry; // Entry Location
    private Location exit;  // Exit Location

    public Maze(int[][] maze, Location entry, Location exit) {

        this.maze = maze;
        numRows = maze.length;
        numCols = maze[0].length;
        visited = new boolean[numRows][numCols]; // initialized to false

        this.entry = entry;
        this.exit = exit;
    }

    public void printMaze() {

        System.out.println("Maze[" + numRows + "][" + numCols + "]");
        System.out.println("Entry index = (" + entry.row + ", " + entry.col + ")");
        System.out.println("Exit index = (" + exit.row + ", " + exit.col + ")" + "\n");

        for (int i = 0; i < numRows; i++) {
            System.out.println(Arrays.toString(maze[i]));
        }
        System.out.println();
    }

    public boolean findPath() {

        return moveTo(entry.row, entry.col);
    }

    private boolean moveTo(int row, int col) {
    	if(row == this.exit.row && col == this.exit.col) {
    		return true;
    	}
    	else if(this.visited[row][col] == false){
        	this.visited[row][col] = true;
        	if(((0 <= row-1 && row - 1 < this.numRows) && this.maze[row-1][col] == 0 && this.visited[row-1][col] == false)) {
         		if(moveTo(row-1,col)) {
        			return true;
        		}
        	}
        	if(((0 <= col+1 && col + 1 < this.numCols) && this.maze[row][col+1] == 0 && this.visited[row][col+1] == false)) {
        		if(moveTo(row,col+1)) {
        			return true;
        		}
        	}
        	if(((0 <= row+1 &&  row + 1 < this.numRows) && this.maze[row+1][col] == 0 && this.visited[row+1][col] == false)) {
        		if(moveTo(row+1,col)) {
        			return true;
        		}
        	}    	
        	if(((0 <= col-1 && col - 1 < this.numCols) && this.maze[row][col-1] == 0 && this.visited[row][col-1] == false)) {
         		if(moveTo(row,col-1)) {
        			return true;
        		}
        	}
        	this.visited[row][col] = false;
    	}return false;
    }

}