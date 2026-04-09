package com.example;
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class AppTest {
    @Test
    public void testEven() {
        App app = new App();
        assertEquals("Even", app.checkEvenOdd(10));
    }
}
