
enum Pebble{
	Red,
	White,
	Blue
}

public class Buckets {
	private Pebble[] pebbles;

	private Pebble color(int i){
		return pebbles[i];
	}

	private int compare(Pebble p){
		Pebble white = Pebble.White;
		return p.ordinal() - white.ordinal();
	}

	private void swap(int i, int j){
		Pebble temp = pebbles[i];
		pebbles[i] = pebbles[j];
		pebbles[j] = temp;
	}

	public void sort(){
		assert pebbles.length > 0;
		int runner = 0, r = 0;
		int b = pebbles.length - 1;

		while(runner <= b){
			int cmp = compare(color(runner));

			if(cmp < 0) swap(runner++, r++);
			else if(cmp > 0) swap(runner, b--);
			else runner++;
		}
	}
}
