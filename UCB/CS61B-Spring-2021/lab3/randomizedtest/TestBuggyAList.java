package randomizedtest;

import edu.princeton.cs.algs4.StdRandom;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Created by hug.
 */
public class TestBuggyAList {
    @org.junit.Test
    public void testThreeAddThreeRemove() {
        AListNoResizing<Integer> list1 = new AListNoResizing<>();
        BuggyAList<Integer> list2 = new BuggyAList<>();

        // 3 addLast()
        for (int i = 0; i < 3; i++) {
            list1.addLast(i);
            list2.addLast(i);
        }

        assertEquals(list1.size(), list2.size());

        assertEquals(list1.removeLast(), list2.removeLast());
        assertEquals(list1.removeLast(), list2.removeLast());
        assertEquals(list1.removeLast(), list2.removeLast());
    }

    @org.junit.Test
    public void randomizedTest() {
        AListNoResizing<Integer> L = new AListNoResizing<>();
        BuggyAList<Integer> anotherL = new BuggyAList<>();

        int N = 5000;
        for (int i = 0; i < N; i += 1) {
            int operationNumber = StdRandom.uniform(0, 4);
            if (operationNumber == 0) {
                // addLast
                int randVal = StdRandom.uniform(0, 100);
                L.addLast(randVal);
                anotherL.addLast(randVal);
                System.out.println("addLast(" + randVal + ")");
            } else if (operationNumber == 1) {
                // size
                int size = L.size();
                int anotherSize = anotherL.size();
                assertEquals(size, anotherSize);
                System.out.println("size: " + size);
            } else if (operationNumber == 2 && L.size() > 0) {
                // getLast
                int lastVal = L.getLast();
                int anotherLastVal = anotherL.getLast();
                assertEquals(lastVal, anotherLastVal);
                System.out.println("getLast(" + lastVal + ")");
            } else if (operationNumber == 3 && L.size() > 0) {
                // removeLast
                int lastVal = L.removeLast();
                int anotherLastVal = anotherL.removeLast();
                assertEquals(lastVal, anotherLastVal);
                System.out.println("removeLast(" + lastVal + ")");
            }
        }
    }
}
