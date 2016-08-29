public static int clock(int hours, int minutes) {
  hours %= 12;
  minutes %= 60;
  return Math.abs(hours * 5 - minutes) * 6;
}
