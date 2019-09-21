// OOP
// Encapsulation
public class Student {
    private String name;
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

// Inheritance
class Person { ... }
class Student extends Person { ... }

// Polymorphism
// Overloading
public class Sum { 
    public int sum(int x, int y) {
        return (x + y); 
    } 
  
    public int sum(int x, int y, int z) {
        return (x + y + z);
    }
}

//Overriding
public class Animal {
    public void move() {
        /* move */ 
    }
}
public class Dog extends Animal {
    public void move() {
        /* move differently */
    }
}

// Abstraction
// Interface
interface Vehicle {
    int getSpeed();
}
public class Bicycle implements Vehicle {
    int speed;
    public int getSpeed() {
        return speed;
    }
}

// Abstract
abstract class Base { 
    abstract void fun(); 
} 
class Derived extends Base { 
    void fun() { 
        System.out.println("fun");
    } 
} 