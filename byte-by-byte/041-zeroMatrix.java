public static void zaroMatrix(boolean[][] matrix) {
  if(matrix.length == 0 || matrix[0].length == 0) return;

  boolean rowZero = false, colZero = false;
  for(boolean b : martix[0]) rowZero |= b;
  for(boolean[] b : matrix) colZero |= b[0];

  for(int i = 1; i < matrix.length; i++) {
    for(int j = 1; j < matrix[0].length; j++) {
      if(matrix[i][j]) {
        matrix[i][0] = true;
        matrix[0][j] = true;
      }
    }
  }

  for(int i = 0; i < matrix.length; i++) {
    if(matrix[i][0]) {
      for(int j = 1; j < matrix[0].length; j++) {
        matrix[i][j] = true;
      }
    }
  }

  for(int j = 0; j < matrix[0].length; j++) {
    if(matrix[0][j]) {
      for(int i = 1; i < matrix.length; i++) {
        matrix[i][j] = true;
      }
    }
  }

  if(rowZero) {
    for(int j = 0; j < matrix[0].length; j++) {
      matrix[0][j] = true;
    }
  }

  if(colZero) {
    for(int i = 0; i < matrix.length; i++) {
      matrix[i][0] = true;
    }
  }

}
