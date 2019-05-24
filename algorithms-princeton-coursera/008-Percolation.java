
public class Percolation {

	public int no;
	public WeightedQuickUnionUF uf;
	public int[] id;

    public Percolation(int N){
	    // create N-by-N grid, with all sites blocked
    	no = N;
    	uf = new WeightedQuickUnionUF(N*N+2);
    	id = new int[N*N+2];
    	id[0] = 1;
    	id[id.length-1] = 1;
    	for(int i = 1; i < id.length-1; i++) {
    		 id[i] = 0;
    	}
    }
    public void open(int i, int j){
	    // open site (row i, column j) if it is not open already
    	if(!isOpen(i,j)){
    		int c = (i-1)*no+j;
    		id[c] = 1;
    		if(i==1){
    			uf.union(0, c);
    			if(isOpen(i+1,j)) uf.union(c, c+no);
    			if(j==1){
    				if(isOpen(i,j+1)) uf.union(c, c+1);
    			} else if(j==no){
    				if(isOpen(i,j-1)) uf.union(c, c-1);
    			} else {
            		if(isOpen(i,j-1)) uf.union(c, c-1);
            		if(isOpen(i,j+1)) uf.union(c, c+1);
    			}
    		} else if(i==no){
    			uf.union(id.length-1, c);
    			if(isOpen(i-1,j)) uf.union(c, c-no);
    			if(j==1){
    				if(isOpen(i,j+1)) uf.union(c, c+1);
    			} else if(j==no){
    				if(isOpen(i,j-1)) uf.union(c, c-1);
    			} else {
            		if(isOpen(i,j-1)) uf.union(c, c-1);
            		if(isOpen(i,j+1)) uf.union(c, c+1);
    			}
    		} else if(j==1){
        		if(isOpen(i,j+1)) uf.union(c, c+1);
        		if(isOpen(i-1,j)) uf.union(c, c-no);
        		if(isOpen(i+1,j)) uf.union(c, c+no);
    		} else if(j==no){
    			if(isOpen(i,j-1)) uf.union(c, c-1);
    			if(isOpen(i-1,j)) uf.union(c, c-no);
        		if(isOpen(i+1,j)) uf.union(c, c+no);
    		} else {
        		if(isOpen(i,j-1)) uf.union(c, c-1);
        		if(isOpen(i,j+1)) uf.union(c, c+1);
        		if(isOpen(i-1,j)) uf.union(c, c-no);
        		if(isOpen(i+1,j)) uf.union(c, c+no);
    		}
    	}
    }
    public boolean isOpen(int i, int j){
    	// is site (row i, column j) open?
	    int c = (i-1)*no+j;
	    if(id[c] == 1) return true;
	    else return false;
    }
    public boolean isFull(int i, int j){
	    // is site (row i, column j) full?
    	int c = (i-1)*no+j;
    	if(uf.root(c) == 0) return true;
    	else return false;
    }
    public boolean percolates(){
	    // does the system percolate?
    	return uf.connected(0, id.length-1);
    }


	public static void main(String[] args) {
		Percolation per = new Percolation(3);
		per.open(1, 1);
		per.open(1, 2);
		per.open(1, 3);
		per.open(2, 1);
		per.open(2, 3);
		per.open(3, 3);
		for(int i = 0; i < per.id.length; i++){
			System.out.print(per.id[i] + " ");
		}
		System.out.println(per.percolates());
		per.uf.print();
	}

}
