package cse2010.homework1;

public class ArraySparseMatrix implements SparseMatrix {

    public static final int DEFAULT_CAPACITY = 1024;

    private int rowCount;
    private int columnCount;
    private int elemCount;
    private Entry[] elements = new Entry[0];

    public ArraySparseMatrix(int rowCount, int columnCount, int capacity) {
        elements = new Entry[capacity];
        this.rowCount = rowCount;
        this.columnCount = columnCount;
        this.elemCount = 0;
    }

    public ArraySparseMatrix(int rowCount, int columnCount) {
        this(rowCount, columnCount, DEFAULT_CAPACITY);
    }

    /*
     * This routine simulates reading from files using two-dimensional matrix.
     */
    public static SparseMatrix create(double[][] aMatrix, int rowCount, int columnCount, int elemCount) {
        ArraySparseMatrix matrix = new ArraySparseMatrix(rowCount, columnCount, elemCount);

        int nonZeroCount = 0;
        for (int i = 0; i < aMatrix.length; i++) {
            for (int j = 0; j < aMatrix[i].length; j++) {
                if (Double.compare(aMatrix[i][j], 0.0) != 0) {
                    matrix.put(new Entry(i, j, aMatrix[i][j]));
                    nonZeroCount++;
                }
            }
    	}
        if(nonZeroCount != elemCount )
        	throw new IllegalStateException("Non zero count doesn't match");
        return matrix;
    }

    private void put(Entry entry) {
        elements[elemCount++] = entry;
    }

    @Override
    public SparseMatrix transpose() {
    	Entry saver1;
    	ArraySparseMatrix result1 = new ArraySparseMatrix(this.columnCount, this.rowCount, this.elemCount);
    	for(int i = 0;i<this.elemCount;i++) {
    		result1.put(new Entry(this.elements[i].getCol(),this.elements[i].getRow(), this.elements[i].getValue()));
    	}
    	for(int i = 0;i<this.elemCount;i++) {
    		for(int j = i+1;j<this.elemCount;j++) {
    			if((result1.elements[i].getRow()*10 + result1.elements[i].getCol()) > result1.elements[j].getRow()*10 + result1.elements[j].getCol()) {
    				saver1 = result1.elements[i];
    				result1.elements[i] = result1.elements[j];
    				result1.elements[j] = saver1;
    			}
    		}
    	}

       return result1;
    }

    @Override
    public SparseMatrix add(SparseMatrix other) {
        if (this.rowCount != other.getRowCount() || this.columnCount != other.getColumnCount())
            throw new IllegalArgumentException("Matrix size doesn't match");
        int count = 0 ;
    	Entry saver2;
        int arr1[] =  new int[DEFAULT_CAPACITY];
        int arr2[] =  new int[DEFAULT_CAPACITY];
        for(int i = 0;i<this.elemCount;i++) {
        	for(int j = 0;j<other.getElemCount();j++) {
        		if((this.elements[i].getRow() == ((ArraySparseMatrix) other).elements[j].getRow()) && (this.elements[i].getCol() == ((ArraySparseMatrix) other).elements[j].getCol())){
        			arr1[count] = i;
        			arr2[count] = j;
        			count++;
        			break;
        		}	
        	}
        }        
        ArraySparseMatrix result2 = new ArraySparseMatrix(this.rowCount, this.columnCount, this.elemCount+other.getElemCount()-count);
        for(int i = 0;i<this.elemCount;i++) {
        	for(int j = 0;j<count;j++) {
        		if(arr1[j] == i) {
        			result2.put(new Entry(this.elements[i].getRow(),this.elements[i].getCol(),this.elements[i].getValue() + ((ArraySparseMatrix)other).elements[arr2[j]].getValue()));
        		}
        		else {
        			result2.put(new Entry(this.elements[i].getRow(),this.elements[i].getCol(),this.elements[i].getValue()));
        		}
        	}
        }
        for(int i =0;i<other.getElemCount();i++) {
        	for(int j = 0;j<count;j++) {
        		if(arr2[j] != i) {
        			result2.put(new Entry(((ArraySparseMatrix) other).elements[i].getRow(),((ArraySparseMatrix) other).elements[i].getCol(),((ArraySparseMatrix) other).elements[i].getValue()));
        		}
        	}
        }
    	for(int i = 0;i<result2.elemCount;i++) {
    		for(int j = i+1;j<result2.elemCount;j++) {
    			if((result2.elements[i].getRow()*10 + result2.elements[i].getCol()) > result2.elements[j].getRow()*10 + result2.elements[j].getCol()) {
    				saver2 = result2.elements[i];
    				result2.elements[i] = result2.elements[j];
    				result2.elements[j] = saver2;
    			}
    		}
    	}        
        return result2;
    }

    public Entry[] getElements() {
        return elements;
    }

    @Override
    public SparseMatrix multiply(SparseMatrix aMatrix) {
        throw new IllegalStateException("Not implemented");
    }

    @Override
    public int getRowCount() {
        return rowCount;
    }

    @Override
    public int getColumnCount() {
        return columnCount;
    }

    @Override
    public int getElemCount() {
        return elemCount;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof ArraySparseMatrix)) return false;
        ArraySparseMatrix other = (ArraySparseMatrix) obj;

        if (rowCount != other.rowCount || columnCount != other.columnCount || elemCount != other.elemCount)
            return false;

        for (int i = 0; i < elements.length; i++) {
            if (!elements[i].equals(other.elements[i])) return false;
        }
        return true;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append(rowCount + "\t" + columnCount + "\t" + elemCount + "\n");
        for (int i = 0; i < elemCount; i ++)
            builder.append(elements[i] + "\n");

        return builder.toString();
    }
}
