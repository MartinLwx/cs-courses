import java.util.Arrays;

public class Hw00 {
    public static void drawTriangle(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                System.out.print('*');
            }
            System.out.println();
        }
    }
    public static int max(int[] m) {
        int maxValue = -1;
        for (int e: m) {
            if (e > maxValue) {
                maxValue = e;
            }
        }
        return maxValue;
    }
    public static void windowPosSum(int[] a, int n) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] < 0) {
                continue;
            } else {
                int windowSum = 0;
                for (int j = i; j <= i + n && j < a.length; j++) {
                    windowSum += a[j];
                }
                a[i] = windowSum;
            }
        }
    }
    public static void main(String[] args) {
        drawTriangle(5);                 // exercise 1a
        drawTriangle(10);                // exercise 1b

        int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6};
        System.out.println(max(numbers));   // exercise 2
        System.out.println(max(numbers));   // exercise 3

        int[] a = {1, 2, -3, 4, 5, 4};      // exercise 4
        windowPosSum(a, 3);
        System.out.println(Arrays.toString(a));
    }
}
