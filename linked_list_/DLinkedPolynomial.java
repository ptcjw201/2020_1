package cse2010.homework2;

import java.util.Arrays;
import java.util.stream.Collectors;

/*
 * © 2020 CSE2010 HW #2
 *
 * You can freely modify this class except the signatures of the public methods!!
 */
public class DLinkedPolynomial implements Polynomial {

    private DLinkedList<Term> list = null;

    public DLinkedPolynomial() {
        list = new DLinkedList<>();
    }

    public int getDegree() {
    	if(this.list.size() == 0) {
    		return 0;
    	}
    	int dgre = 0;
    	Node<Term> current = this.list.getFirstNode();
    	do {
    		if(dgre < current.getInfo().expo) {
    			dgre = current.getInfo().expo;
    		}
    		current = this.list.getNextNode(current);
    	}while(current != null);
		return dgre;
    }

    @Override
    public double getCoefficient(final int expo) {
        Node<Term> term = list.find(new Term(0.0, expo), Term::compareExponents);
        if (term == null) {
        	return 0;
        }
        return term.getInfo().coeff;
    }

    private Term addTerms(Term x, Term y) {
        return new Term(x.coeff + y.coeff, x.expo);
    }

    @Override
    public Polynomial add(final Polynomial p) {
    	Polynomial res = new DLinkedPolynomial();
    	DLinkedPolynomial copy = (DLinkedPolynomial)p;
    	Node<Term> current = this.list.getFirstNode();
    	Node<Term> current2 = copy.list.getFirstNode();
    	while(current2 != null) {
    		res.addTerm(current2.getInfo().coeff, current2.getInfo().expo);
    		current2 = copy.list.getNextNode(current2);
    	}
    	current2 = copy.list.getFirstNode();
    	do {
    		res.addTerm(current.getInfo().coeff, current.getInfo().expo);
    		current = this.list.getNextNode(current);
    	}while(current != null);
        return res; 
    }

    private Term multTerms(Term x, Term y) {
        return new Term(x.coeff * y.coeff, x.expo + y.expo);
    }

    @Override
    public Polynomial mult(final Polynomial p) {
    	Polynomial res = new DLinkedPolynomial();
    	DLinkedPolynomial copy = (DLinkedPolynomial)p;
    	Node<Term> current = this.list.getFirstNode();
    	Node<Term> current2;
    	while(current != null) {
        	current2 = copy.list.getFirstNode();
    		while(current2 != null) {
    			res.addTerm(current.getInfo().coeff * current2.getInfo().coeff, current.getInfo().expo + current2.getInfo().expo);
    			current2 = copy.list.getNextNode(current2);
    		}
    		current = this.list.getNextNode(current);
    	}
		return res;
    }

    @Override
    public void addTerm(final double coeff, final int expo) {
    	Term trm = new Term(coeff, expo); 
	  	Node<Term> newnode = new Node<Term>(trm);
	  	Node<Term> current = this.list.getFirstNode();
    	if(this.list.isEmpty()) {
    		this.list.addFirst(newnode);
    	}
    	else {
    		for(int i = 0;i<this.termCount();i++) {
    			if(current.getInfo().expo == expo) {
    				current.getInfo().coeff = current.getInfo().coeff + coeff;
    				break;
    			}
    			else if(current.getInfo().expo<expo) {
    				this.list.addBefore(current, newnode);
    				break;
    			}
    			else if(current.getInfo().expo>expo) {
    				if(current.equals(list.getLastNode())) {
    					list.addLast(newnode);
    					break;
    				}
    				else if(expo>current.getNext().getInfo().expo){
    					list.addAfter(current, newnode);
    					break;
    				}
    			}
    			current = this.list.getNextNode(current);
    		}
    	}
    }

	@Override
    public void removeTerm(final int expo) {
        Node<Term> node = list.find(new Term(0, expo), Term::compareExponents);
        Node<Term> temp = this.list.getFirstNode();
        if(node == null) {
            throw new NoSuchTermExistsException();
        }
        while(true) {
        	if(temp.equals(node)) {
        		this.list.remove(node);
        		return;
        	}
        	temp = this.list.getNextNode(temp);
        }	
    }

    @Override
    public int termCount() {
        return list.size();
    }

    @Override
    public double evaluate(final double val) {
        double rlt = 0.0;
        Node<Term> current = this.list.getFirstNode();
        while(current != null) {
        	rlt = rlt + Math.pow(val,current.getInfo().expo) * current.getInfo().coeff;
        	current = this.list.getNextNode(current);
        }
        return rlt;
    }

    @Override
    public String toString() {
        if (list.isEmpty())
            return "Empty Polynomial";
        else {
            String[] terms = new String[termCount()];
            int i = 0;
            Node<Term> current = list.getFirstNode();
            do {
                if (current.getInfo().expo == 0) {
                    terms[i++] = String.valueOf(current.getInfo().coeff);
                } else if (current.getInfo().expo == 1) {
                    terms[i++] = current.getInfo().coeff + "x";
                } else {
                    terms[i++] = current.getInfo().coeff + "x^" + current.getInfo().expo;
                }
                current = list.getNextNode(current);
            } while (current != null);
            return String.join("+", terms);
        }
    }

}

