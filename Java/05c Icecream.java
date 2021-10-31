public class Icecream {
	public static void main(String[] args) {
	    int count = 0; //Total number of cones
	    int scount = 0; //Number of strawberry cones
	    TextIO.readFile("E:/icecream.dat");  // Read from the file.
	    do {	//Parsing each line of the file until the end is reached
	    count++;
	    String flavor = TextIO.getln();  // Reads the current line of the file.
	    if(flavor.equals("Strawberry"))
	    {
	    	scount++;
	    }
	    }while(!TextIO.eof());

	    double percentage = ((double)scount/count)*100; //Percentage of strawberry cones.
	    
	    System.out.println("Total number of cones is "+ count);
	    System.out.println("Number of Strawberry cones is " + scount);
	    System.out.printf("The percentage of cones that was strawberry is %1.1f ", percentage);
	    System.out.println();
	}

}