import java.util.*;

class tictactoe {
    void print(String[] grid) {
        System.out.println("┌─┬─┬─┐");
        System.out.println("│" + grid[0] + "│" + grid[1] + "│" + grid[2] + "│");
        System.out.println("├─┼─┼─┤");
        System.out.println("│" + grid[3] + "│" + grid[4] + "│" + grid[5] + "│");
        System.out.println("│─┼─┼─┤");
        System.out.println("│" + grid[6] + "│" + grid[7] + "│" + grid[8] + "│");
        System.out.println("└─┴─┴─┘");

        System.out.println("This is the table,enter the corresponding number to enter X and O ");
    } 
    String check(String[] grid) {
        // Check rows
        if (grid[0] == grid[1] && grid[0] == grid[2])
            return grid[0];
        if (grid[3] == grid[4] && grid[3] == grid[5])
            return grid[3];
        if (grid[6] == grid[7] && grid[6] == grid[8])
            return grid[6];
        
        // Check columns
        if (grid[0] == grid[3] && grid[0] == grid[6])
            return grid[0];
        if (grid[1] == grid[4] && grid[1] == grid[7])
            return grid[1];
        if (grid[2] == grid[5] && grid[2] == grid[8])
            return grid[2];
        
        // Check diagonals
        if (grid[0] == grid[4] && grid[0] == grid[8])
            return grid[0];
        if (grid[2] == grid[4] && grid[2] == grid[6])
            return grid[2];
        
        boolean spaceFound = false;
        for (int i = 0; i < 9; i++) {
            if (grid[i] != "X" || grid[i] != "O") {
                spaceFound = true;
                break;
            }
        }

        if (spaceFound == false)
            return "tie";

        return "none";
    }
    public static void main(String args[]) {
        int chance = 0;
        int choice = 0;
        String current = "";
        String grid[] = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
        Scanner s = new Scanner(System.in);
        tictactoe obj = new tictactoe();

        System.out.println("Welcome to the game of tic tac toe!");

        while (obj.check(grid) == "none") {
            obj.print(grid);
            System.out.println("Enter the space you want to choose.");
            choice = s.nextInt() - 1;

            while (choice > 8 || choice < 0) {
                System.out.println("Please enter a number available in the board.");
                choice = s.nextInt() - 1;
            }
            while (grid[choice] == "X" || grid[choice] == "O") {
                System.out.println("That space is already occupied. Please choose another one.");
                choice = s.nextInt();
            }         

            current = (chance % 2 == 0) ? "X" : "O";

            grid[choice] = current;
            chance++;
        }

        obj.print(grid);
        String result = obj.check(grid);
        if (result == "tie")
            System.out.println("The game ended in a tie.");
        else
            System.out.println(result + " won the game!");
    }
}