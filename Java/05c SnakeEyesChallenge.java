public class SnakeEyesChallenge {
	public static void main(String[] args) {
		
		int sum = 0;
		for(int i = 1; i <= 1000 ; i++)	//Simulating thousand attempts at getting snake eyes.
		{
			sum+= roll();	//In order to find average, we first find the sum
		}
		
		System.out.println("Average number of events it took to reach snakes eye is " + (int)sum/1000);	//Avg. is calculated and printed.									   
		
	}
	
	public static int roll() { //This subroutine is the same as the program 'SnakeEyes'. Instead of printing the answer, it returns.
		int events = 0;	//No. of events it took to get a snake eyes outcome
		int die1, die2;
		do
		{
			die1 = (int)(Math.random()*6)+1;
			die2 = (int)(Math.random()*6)+1;
			events++;
			if(die1 == 1 && die2 == 1)
			{
				break;
			}
		}while(true); //continue rolling if both die are not 1
		
		return events;


		} // End of roll method
}//End of class
