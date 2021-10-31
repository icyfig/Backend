import java.util.Scanner;
public class battleship
{
    int[][] player = new int[3][3];
    int[][] computer = new int[3][3];
    public  void main()
    {
        Scanner kb = new Scanner(System.in);
        System.out.println("Welcome to battleShips! '*' represents a failed attempt, '~'unattempted,'X' a successful");
        System.out.println(" attempt and 's' a ship. Now let's arrange your board with 3 ships of length 3.");
        
        for(int i = 0; i<2;i++)//player arranging ships
        {
            System.out.println(i+"th/st/nd ship:");
            for(int j = 0; j< 1; j++)//orientation of a ship
            {
                System.out.println(j+"th/st/nd position:");
                player[i][j] = kb.nextInt();
            }
        }
        initializeComputer();
        displayPlayer();//display the player's board.
    }
    public void initializeComputer()
    {

        for(int i = 0; i< 3;i++)
        {
           int startRow = (int) Math.floor(Math.random() * 6); // a random position on board
           int startColumn = (int) Math.floor(Math.random() * 6); // a random position on board
           
           if(startRow + 2 < 6) //fits in board
           {
               computer[i][0] = startRow;
               computer[i][1] = startRow+1;//ship formed in straight line
               computer[i][2] = startRow+2;
           }
           else
           {
               if(startColumn + 2 < 6)
               {
                   computer[i][0] = startColumn;
                   computer[i][1] = startColumn+1;
                   computer[i][2] = startColumn+2;
               }
               else
               {
                   computer[i][0] = startRow;
                   computer[i][1] = startRow-1;
                   computer[i][2] = startRow-2;
               }
           }
        }
    }
    public void displayPlayer()
    {
        for(int i = 0 ; i<5;i++) // printing rows
        {
            System.out.print(i); // row number
            for(int j = 0; j<40;j++) //40 dashes in each row
            {
                if(j>6 && (j-1)%7 == 0 )
                    System.out.print("|");
                else
                    System.out.print("-");
            }
            System.out.println();
        }
    }
}
    