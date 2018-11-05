abstract class Animal {
  private int order;
  protected String name;

  public Animal(String name) { this.name = name; }
  public void setOrder(int order) { this.order = order; }
  public int getOrder() { return order; }

  /* Compare orders of animals to return the older item. */
  public boolean isOlderThan(Animal a) { return this.order < a.getOrder(); }
}

class AnimalQueue {
  LinkedList<Dog> dogs = new LinkedList<>();
  LinkedList<Cat> cats = new LinkedList<>();
  private int order = 0; // acts as timestamp

  public void enqueue(Animal animal) {
    /* Order is used as a sort of timestamp, so that we can compare the insertion
     * order of a dog to a cat. */
    animal.setOrder(order++);

    if (animal instanceOf Dog) dogs.addLast(animal);
    else if (animal instanceOf Cat) cats.addLast(animal);
  }

  public Animal dequeueAny() {
    if (dogs.size() == 0) return dequeueCat();
    else if (cats.size() == 0) return dequeueDog();

    /* Look at tops of dog and cat queues, and pop the queue with the oldest
     * value. */
    Dog dog = dogs.peek();
    Cat cat = cats.peek();
    if (dog.isOlderThan(cat)) return dequeueDog();
    else return dequeueCat();
  }

  public Dog dequeueDog() {
    dogs.poll();
  }

  public Cat dequeueCat() {
    cats.poll();
  }
}

public class Dog extends Animal {
  public Dog(String name) { super(name); }
}

public class Cat extends Animal {
  public Cat(String name) { super(name); }
}
