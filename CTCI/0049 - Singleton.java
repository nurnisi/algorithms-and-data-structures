public class Singleton {
    private static Singleton _instance = null;
    protected Singleton() { ... }
    public static Singleton getInstance() {
        if (_instance == null) {
            _instance = new Singleton();
        }
        return _instance;
    }
}