import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;

import org.json.simple.parser.ParseException;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import org.json.simple.parser.JSONParser;

public class PrescriptionManagement {



  public static void main(String[] args) throws IOException, ParseException {


	   BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      int choice, numMedications;
      Prescription prescription = new Prescription();


     while(true) {

        while(true) {

           // TODO: Add code to display the menu and get the number(choice) a user selected
            BufferedReader inp = new BufferedReader (new InputStreamReader(System.in));
            System.out.println("Menu:");
            System.out.println("\t1. Add Prescription");
            System.out.println("\t2. View Prescriptions");
            System.out.println("\t3. Delete Prescription");
            System.out.println("\t4. Exit");


            choice = Integer.parseInt(inp.readLine());



           switch (choice) {
              case 1:

                  String pID, cID, doctorsName;
                  System.out.println("Enter the prescription ID: ");
                  pID = inp.readLine();
                  System.out.println("Enter the customer ID: ");
                  cID = inp.readLine();
                  System.out.println("Enter the Doctor's name: ");
                  doctorsName = inp.readLine();

                  prescription.setPrescriptionID(pID);
                  prescription.setCustomerID(cID);
                  prescription.setDoctorName(doctorsName);




                  prescription.setDate(LocalDate.now());


                  System.out.print("Enter the number of medications to add: ");
                  numMedications = Integer.parseInt(reader.readLine());

                  ArrayList<Medication> medications = new ArrayList<>();
                  String medicationName, medicationDetails, dosage, medicationID;
                  int quantity;


                  // TODO: Add code to display available products/medications before adding them on the prescription
                  String medicationsFilePath = "products.json";
                  // TODO: Add code to display the available medications in a table format so that the user
                  // can easily select.
                  PrescriptionManagement.displayMedications(medicationsFilePath);

                  for (int i = 1; i <= numMedications; i++) {

                      System.out.println("Enter details for Medication " + i + ":");

                       // TODO: Add code to get Medication ID, Name, Details, Dosage and Quantity

                      System.out.println("ID: ");
                      medicationID = inp.readLine();
                      System.out.println("Name: ");
                      medicationName = inp.readLine();
                      System.out.println("Details: ");
                      medicationDetails = inp.readLine();
                      System.out.println("Dosage: ");
                      dosage = inp.readLine();
                      System.out.println("Quantity: ");
                      quantity = Integer.parseInt(inp.readLine());


                      Medication medication = new Medication(medicationID, medicationName, medicationDetails, dosage, quantity);
                      medications.add(medication);
                   }

                   // TODO: Add code to save all medications inserted by the user on the prescription
                  prescription.setMedications(medications);


                  prescription.addPrescription();

                  break;
              case 2:

                  ArrayList<Prescription> prescriptions = prescription.viewPrescription(); // TODO: Check if this assignment works
                  if(prescriptions.size()==0) {
                      System.out.println("No prescriptions available\n");
                  }
                  else {
                      System.out.println("| PrescriptionID |  DoctorName   |    CustomerID | \tDate\t | ");
                      System.out.println("******************************************************************");

                      for(Prescription p: prescriptions)
                      {
                          System.out.println("|\t  "+ p.getPrescriptionID()+"\t\t"+ p.getDoctorName()+ "\t\t  " + p.getCustomerID()+"\t\t" + p.getDate());

                          System.out.println("");
                          System.out.println("| MedicationID |  \tName    | \t Quantity | ");
                          for(Medication med : p.getMedications())
                          {
                              System.out.println("|\t  "+ med.getID()+"\t\t"+ med.getName()+ "\t\t " + med.getQuantity() );
                          }

                          System.out.print("\n");
                          System.out.println("*****************************************************************");
                      }

                      System.out.println("");
                  }

           	   break;
              case 3:
                  String prescrID;
                  System.out.println("Enter the prescription ID to delete: ");
                  prescrID = inp.readLine();
                  prescription.deletePrescription(prescrID);
                 break;
              case 4:
                  System.out.println("Exiting the Prescription Management section...");
                  System.exit(0);
              default:
                 System.out.println("Invalid choice. Please try again.");
           }


        }


     }
  }



  public static void displayMedications(String filePath) throws FileNotFoundException, IOException, ParseException {

	      JSONParser parser = new JSONParser();
	      try(FileReader fileReader = new FileReader(filePath)){
	          if (fileReader.read() == -1) {
	              return;
	          }
	          else {
	              fileReader.close();
	              JSONArray jsonArray = (JSONArray) parser.parse(new FileReader(filePath));

                 System.out.println("---------------------------------------------------------------------------------------");
                 System.out.println("|\t"  + "\t\t  "  + "\t\t\t\t");
                 System.out.println("|\t" + "\t\t"  +  "Available Medications" + "\t\t");
                 System.out.println("|\t"  + "\t\t  "  + "\t\t\t\t");
                 System.out.println("---------------------------------------------------------------------------------------");
                 System.out.println("| Medication ID |  Medication Name   |    Medication Price ||    Medication Quantity |");
                 System.out.println("---------------------------------------------------------------------------------------");

	              for (Object obj: jsonArray) {
	                  JSONObject jsonObject = (JSONObject) obj;


                    String medicationID = (String) jsonObject.get("code");
                    String medicationName = (String) jsonObject.get("name");
                    String medicationPrice = (String) jsonObject.get("price");
                    String medicationQuantity = (String) jsonObject.get("quantity");

                    System.out.println("|\t" + medicationID + "\t\t" + medicationName + "\t\t  " + medicationPrice + "\t\t\t  " + medicationQuantity + "\t\t");

	              }
                 System.out.println("---------------------------------------------------------------------------------------");


	          }
	      }

  }


}
