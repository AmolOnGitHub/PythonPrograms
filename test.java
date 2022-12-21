import java.time.*;
import java.util.Scanner;

class date90 {
    static String printDate(LocalDate d) {
        String s = d.getDayOfMonth() + "/";
        s += d.getMonthValue() + "/";
        s += d.getYear();
        return s;
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.println("Enter the date: (DD/MM/YYYY)");
        String input = s.next();
        String[] dmy = input.split("/");

        int year = Integer.parseInt(dmy[2]);
        int month = Integer.parseInt(dmy[1]);
        int day = Integer.parseInt(dmy[0]);

        LocalDate ld = LocalDate.of(year, month, day);
        LocalDate delta = ld.plusDays(90);

        System.out.println("Original Date: " + printDate(ld) + " " + ld.getDayOfWeek());
        System.out.println("New Date: " + printDate(delta) + " " + delta.getDayOfWeek());        
    }
}