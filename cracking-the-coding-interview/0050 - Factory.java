public class Factory {
    public static Factory createInstance(InstanceType type) {
        if (type == InstanceType.Poker) {
            return new PokerGame();
        } else if (type == InstanceType.BlackJack) {
            return new BlackJack();
        }
        return null;
    }
}