package cse2010.homework5;
import java.util.Stack;


public class SyntaxTree extends LinkedBinaryTree<String> {

    public static SyntaxTree buildSyntaxTree(String[] expr) {
    	int len = expr.length;
    	Node op1 = new Node(null,null,null,null);
    	Node op2 = new Node(null,null,null,null);
    	SyntaxTree snt = new SyntaxTree();
    	snt.size = 0;
    	Stack<Node> st = new Stack(); 
    	for(int k = 0;k<len;k++) {
    		if(expr[k].charAt(0) != '+' && expr[k].charAt(0) != '-' && expr[k].charAt(0) != '*' && expr[k].charAt(0) != '/') {
        		Node newnode = new Node(expr[k],null,null,null);
        		st.push(newnode);
    		}else {
				op1 = st.pop();
				op2 = st.pop();
    			Node newnode1 = new Node(expr[k],null,op2,op1);
    			op1.setParent(newnode1);
    			op2.setParent(newnode1);
    			st.push(newnode1);    			
    		}
    		snt.size++;
    		snt.root = st.peek();
    	}
    	return snt;
    }

    public void making_par(Stack stck, Node nn) {
    	if(nn!=null) {
    		if(((String)nn.getElement()).charAt(0) != '+' && ((String)nn.getElement()).charAt(0) != '-' && ((String)nn.getElement()).charAt(0) != '*' && ((String)nn.getElement()).charAt(0) != '/') {
    			stck.push((String)nn.getElement());
    		}
    		else {
    			stck.push("(");
    			making_par(stck,nn.getLeft());  			
    			stck.push(" " + (String)nn.getElement() + " ");
    			making_par(stck,nn.getRight());
    			stck.push(")");
    		}			
    	}
    }
    
    public String parenthesize() {
    	Object[] ans;
    	String par_result = "";
    	Stack<String> par_stck = new Stack();
    	making_par(par_stck, this.root);
    	ans = par_stck.toArray();
    	for(int i = 0;i<ans.length;i++) {
    		par_result+=ans[i];
    	}
    	return par_result;
    }

    public double eval_helper(Node nn) {
		if(isInternal(nn)) {
			double op1 = eval_helper(nn.getLeft());
			double op2 = eval_helper(nn.getRight());
			switch((String)nn.getElement()) {
			case "+":
				return op1+op2;
			case "-":
				return op1-op2;
			case "*":
				return op1*op2;
			default:
				return op1/op2;
			}
		}
		else {
			return Double.valueOf(nn.getElement().toString());
		}
	}
    
    public double evaluate() {
    	double ans;
    	ans = eval_helper(this.root);
    	return ans;
    }

    
    public void making_prefix(Stack stck, Node nn) {
    	if(nn!=null) {
    		if(((String)nn.getElement()).charAt(0) != '+' && ((String)nn.getElement()).charAt(0) != '-' && ((String)nn.getElement()).charAt(0) != '*' && ((String)nn.getElement()).charAt(0) != '/') {
    			stck.push(" "+(String)nn.getElement());
    		}
    		else {
    			if(nn == this.root) {
        			stck.push((String)nn.getElement());
    			}else {
        			stck.push(" "+(String)nn.getElement());    				
    			}
    			making_prefix(stck,nn.getLeft());  			
    			making_prefix(stck,nn.getRight());;
    		}			
    	}
    }
    
    public String toPrefix() {
    	Object[] ans_pref;
    	String pre_res = "";
        Stack<String> st_pre = new Stack();
        making_prefix(st_pre, this.root);
        ans_pref = st_pre.toArray();
    	for(int i = 0;i<ans_pref.length;i++) {
    		pre_res+=ans_pref[i];
    	}
    	return pre_res;
    }

    
    public void making_ind(Stack stck, Node nn) {
    	if(nn!=null) {
    		String add = "";
    		if(((String)nn.getElement()).charAt(0) != '+' && ((String)nn.getElement()).charAt(0) != '-' && ((String)nn.getElement()).charAt(0) != '*' && ((String)nn.getElement()).charAt(0) != '/') {
    			for(int i = 0;i<depth(nn);i++) {
    				add+="  ";
    			}
    			stck.push(add + (String)nn.getElement()+ '\n');
    		}
    		else {			
    			for(int i = 0;i<depth(nn);i++) {
    				add+="  ";
    			}
    			stck.push(add  + (String)nn.getElement() + "\n");
    			making_ind(stck,nn.getLeft());  
    			making_ind(stck,nn.getRight());
    		}			
    	}
    }
    
    
    public String indentSyntaxTree() {
    	Object[] ans;
    	String ind_res = "";
    	Stack<String> ind_stck = new Stack();
    	making_ind(ind_stck, this.root);
    	ans = ind_stck.toArray();
    	for(int i = 0;i<ans.length;i++) {
    		ind_res+=ans[i];
    	}
    	return ind_res;
    }

    public static void main(String... args) {

        System.out.println("Homework 5");
    }
}


