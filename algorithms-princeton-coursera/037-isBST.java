
public boolean isBST(Node x, Key min, Key max) {
	if(x == null) return true;
	if(less(max, x.key) || less(x.key, min)) return false;
	return isBST(x.left, min, x.key) && isBST(x.right, x.key, max);
}

private boolean less(Key i, Key j) {
	return i.compareTo(j) < 0;
}
