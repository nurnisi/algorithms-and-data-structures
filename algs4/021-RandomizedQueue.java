
import java.util.Iterator;
import java.util.NoSuchElementException;

import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {
	private Item[] s;
	private int head, tail, N;

	public RandomizedQueue() {
		// construct an empty randomized queue
		s = (Item[]) new Object[1];
		N = head = tail = 0;
	}
	public boolean isEmpty() {
		// is the queue empty?
		return N == 0;
	}
	public int size() {
		// return the number of items on the queue
		return N;
	}

	private void resize(int capacity) {
		Item[] copy = (Item[]) new Object[capacity];
		int j = 0;
		while(head < tail){
			copy[j++] = s[head++];
		}
		s = copy;
		head = 0;
		tail = j;
	}

	public void enqueue(Item item) {
		// add the item
		if(tail == s.length) resize(tail-head*2);
		s[tail++] = item;
		N++;
	}

	public Item dequeue() {
		// remove and return a random item
		int r = StdRandom.uniform(head, tail);
		swap(head, r);
		Item item = s[head];
		s[head++] = null;
		N--;
		if(N>0 && N==s.length/4) resize(s.length/2);
		return item;
	}

	private void swap(int i, int j) {
		Item swap = s[i];
		s[i] = s[j];
		s[j] = swap;
	}

	public Item sample() {
		// return (but do not remove) a random item
		int r = StdRandom.uniform(N);
		return s[r];
	}

	public Iterator<Item> iterator() {
		// return an independent iterator over items in random order
		return new ArrayIterator();
	}

	private class ArrayIterator implements Iterator<Item> {
		private int i = 0;
		private Item[] temp;

		public ArrayIterator() {
			temp = (Item[]) new Object[N];
			for(int j = head; j < tail; j++)
				temp[j] = s[j];
			StdRandom.shuffle(temp);
		}

		@Override
		public boolean hasNext() {
			return i<N;
		}

		@Override
		public Item next() {
			if(!hasNext()) throw new NoSuchElementException();
			return temp[i++];
		}

	}
}
