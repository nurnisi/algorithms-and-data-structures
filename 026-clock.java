//by me
public static int clock(int hours, int minutes) {
  hours %= 12;
  minutes %= 60;
  return Math.abs(hours * 5 - minutes) * 6;
}
//by sam
public static double clock(int hours, int minutes) {
  final double MINUTES_PER_HOUR = 60;
  final double DEGREES_PER_MINUTE = 360 / MINUTES_PER_HOUR;
  final double DEGREES_PER_HOUR = 360 / 12;

  double minutesAngle = minutes * DEGREES_PER_MINUTE;
  double hoursAngle = hours * DEGREES_PER_HOUR + (minutes / MINUTES_PER_HOUR) * DEGREES_PER_HOUR;

  double diff = Math.abs(minutesAngle - hoursAngle);
  if(diff > 180) return 360 - diff;
  return diff; 
}
