public class isBST {

  private class Node {
    int data;
    Node leftChild;
    Node rightChild;
  }

  private Node root = null;

  public void insert(int newData) {
    Node newNode;
    Node current;
    Node parent;

    newNode.data = newData;
    newNode.leftChild = null;
    newNode.rightChild = null;

    if(root == null) root = newNode;
    else {
      current = root;
      parent = null;

      while(true) {
        parent = current;

        if(newData < current.data) {
          current = current.leftChild;
          if(current = null) {
            parent.leftChild = newNode;
            return;
          }
        } else {
          current = current.rightChild;
          if(current == null) {
            parent.rightChild = newNode;
            return;
          }
        }
      }
    }
  }

  public int search(int data) {
    Node current = root;
    while(data != current.data) {
      if(data < current.data) {
        current = current.leftChild;
      } else {
        current = current;rightChild;
      }

      if(current == null) return null;
    }

    return current.data;
  }

  public boolean isBST(Node current) {
    if(current == null) return;
    if(current.leftChild != null) {
      if(current.leftChild.data > current.data) return false;
      isBST(current.leftChild);
    }
    if(current.rightChild != null) {
      if(current.rightChild.data < current.data) return false;
      isBST(current.rightChild);
    }
  }

  public boolean isBSTbySam(Node root) {
    return isBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
  }

  private boolean isBST(Node n, int min, int max) {
    if(n == null) return true;
    if(n.value < min || n.value > max) return false;
    return isBST(n.leftChild, min, n.value) && is(n.rightChild, n.value + 1, max);
  }

}
