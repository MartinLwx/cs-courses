package IntList;

import static org.junit.Assert.*;
import org.junit.Test;

public class SquarePrimesTest {

    /**
     * Here is a test for isPrime method. Try running it.
     * It passes, but the starter code implementation of isPrime
     * is broken. Write your own JUnit Test to try to uncover the bug!
     */
    @Test
    public void testSquarePrimesSimple() {
        IntList lst = IntList.of(2, 3, 8, 11, 14);
        boolean changed = IntListExercises.squarePrimes(lst);
        assertEquals("4 -> 9 -> 8 -> 121 -> 14", lst.toString());
        assertTrue(changed);
    }
}
