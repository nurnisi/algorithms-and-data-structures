//Permutaions for strings
public ArrayList<String> permutations(String s) {
  ArrayList<String> result = new ArrayList<String>();
  permutations(prefix, suffix, result);
  return result;
}

private void permutations(String prefix, String suffix, ArrayList<String> result) {
  if(suffix.length == 0) {
    result.add(prefix);
  } else {
    for(int i = 0, i < suffix.length; i++) {
      permutations(prefix + suffix.charAt(i), suffix.substring(0, i) + suffix.substring(i+1, suffix.length, result);
    }
  }
}

//Permutations for integers
public ArrayList<int[]> permutations(int[] a) {
  ArrayList<int[]> result = new ArrayList<int[]>();
  permutations(a, o, result);
  return result;
}

private void permutations(int[] a, int start, ArrayList<int[]> result) {
  if(start >= a.length) {
    result.add(a);
  } else {
    for(int i = start; i < a.length; i++) {
      swap(a, start, i);
      permutations(a, start + 1, result);
      swap(a, start, i);
    }
  }
}

private swap(int[] a, int i, int j) {
  int temp = a[i];
  a[i] = a[j];
  a[j] = temp;
}
