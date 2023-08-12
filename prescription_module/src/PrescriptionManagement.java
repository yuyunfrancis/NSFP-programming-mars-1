import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.LocalDate;
import java.util.ArrayList;

import org.json.simple.parser.ParseException;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import org.json.simple.parser.JSONParser;

public class PrescriptionManagement {


   public static void main(String[] args) throws IOException, ParseException {


       BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
       int choice = 0, numMedications;
       Prescription prescription = new Prescription();
       FileHandler fileHandler = new FileHandler();

       while (true) {
           System.out.println("Prescription Management System");
           System.out.println("1. Add Prescription");
           System.out.println("2. View Prescriptions");
           System.out.println("3. Delete Prescription");
           System.out.println("4. Exit");
           System.out.print("Enter your choice: ");

           String input = reader.readLine();
           if (input == null || input.isEmpty()) {
               System.out.println("Invalid input");
               break;
           }
           try {
               choice = Integer.parseInt(input);
           } catch (NumberFormatException e) {
               System.out.println("Invalid input");
               break;
           }

           // TODO: Add code to display the menu and get the number(choice) a user slected

                   // TODO: Add code to get Prescription ID, Customer ID,  Doctor's Na
           switch (choice) {
                       case 1:
                           System.out.println("Add Prescription");
                           System.out.print("Enter Prescription ID: ");
                           String prescriptionID = reader.readLine();
                           if (prescriptionID == null || prescriptionID.isEmpty()) {
                               System.out.println("Invalid input");
                               break;
                           }
                           prescription.setPrescriptionID(prescriptionID);

                           System.out.print("Enter Customer ID: ");
                           String customerID = reader.readLine();
                           if (customerID == null || customerID.isEmpty()) {
                               System.out.println("Invalid input");
                               break;
                           }
                           prescription.setCustomerID(customerID);

                           System.out.print("Enter Doctor's Name: ");
                           String doctorName = reader.readLine();
                           if (doctorName == null || doctorName.isEmpty()) {
                               System.out.println("Invalid input");
                               break;
                           }
                           prescription.setDoctorName(doctorName);

                           System.out.print("Enter the number of medications to add: ");
                           String numberOfMeds = reader.readLine();
                           if (numberOfMeds == null || numberOfMeds.isEmpty()) {
                               System.out.println("Invalid input");
                               break;
                           }
                           try {
                               numMedications = Integer.parseInt(input);
                           } catch (NumberFormatException e) {
                               System.out.println("Invalid input");
                               break;
                           }

                           ArrayList<Medication> medications = new ArrayList<>();

                           displayMedications("src/products.json");

                           for (int i = 1; i <= numMedications; i++) {
                               String medicationName, medicationDetails, dosage, medicationID;
                               int quantity;
                               System.out.println("Enter Medication " + i + " details");
                               System.out.print("Enter Medication ID: ");
                               medicationID = reader.readLine();
                               if (medicationID == null || medicationID.isEmpty()) {
                                   System.out.println("Invalid input");
                                   break;
                               }
                               System.out.print("Enter Medication Name: ");
                               medicationName = reader.readLine();
                               if (medicationName == null || medicationName.isEmpty()) {
                                   System.out.println("Invalid input");
                                   break;
                               }
                               System.out.print("Enter Medication Details: ");
                               medicationDetails = reader.readLine();
                               if (medicationDetails == null || medicationDetails.isEmpty()) {
                                   System.out.println("Invalid input");
                                   break;
                               }
                               System.out.print("Enter Dosage: ");
                               String medDose = reader.readLine();
                               if (medDose == null || medDose.isEmpty()) {
                                   System.out.println("Invalid input");
                                   break;
                               }
                               System.out.print("Enter Quantity: ");
                               String quantityString = reader.readLine();
                               if (quantityString == null || quantityString.isEmpty()) {
                                   System.out.println("Invalid input");
                                   break;
                               }
                               try {
                                   quantity = Integer.parseInt(quantityString);
                               } catch (NumberFormatException e) {
                                   System.out.println("Invalid input");
                                   break;
                               }
                               dosage = medDose.trim();
                               Medication medication = new Medication(medicationID, medicationName, medicationDetails, dosage, quantity);
                               medications.add(medication);
                           }

                            prescription.setMedications(medications);
                           prescription.addPrescription();
                           System.out.println("Prescription added successfully\n");
                           // Don't forget to add code to save these information in the prescription

                           break;
                       case 2:
                           // TODO: Add code to retrieve all prescriptions in the file
                           // Prescriptions must be returned in the array
                           ArrayList<Prescription> prescriptions = new ArrayList<>();
                            prescriptions = prescription.viewPrescription();

                           if (prescriptions.size() == 0) {
                               System.out.println("No precriptions available\n");
                           } else {
                               System.out.println("| PrescriptionID |  DoctorName   |    CustomerID | \tDate\t | ");
                               System.out.println("******************************************************************");

                               for (Prescription p : prescriptions) {
                                   System.out.println("|\t  " + p.getPrescriptionID() + "\t\t" + p.getDoctorName() + "\t\t  " + p.getCustomerID() + "\t\t" + p.getDate());

                                   System.out.println("");
                                   System.out.println("| MedicationID |  \tName    | \t Quantity | ");
                                   for (Medication med : p.getMedications()) {
                                       System.out.println("|\t  " + med.getID() + "\t\t" + med.getName() + "\t\t " + med.getQuantity());
                                   }

                                   System.out.print("\n");
                                   System.out.println("*****************************************************************");
                               }

                               System.out.println("");
                           }

                           break;
                       case 3:
                           // TODO: Add code to get the ID of the prescription you want to delete
                           System.out.print("Enter the ID of the prescription you want to delete: ");
                            String prescrID = reader.readLine();
                            if (prescrID == null || prescrID.isEmpty()) {
                                System.out.println("Invalid input");
                                break;
                            }

                           prescription.deletePrescription(prescrID);
                           break;
                       case 4:
                           System.out.println("Exiting the Precription Management section...");
                           System.exit(0);
                       default:
                           System.out.println("Invalid choice. Please try again.");
                   }


           }

       }
   public static void displayMedications(String filePath) throws FileNotFoundException, IOException, ParseException {

       JSONParser parser = new JSONParser();
       try (FileReader fileReader = new FileReader(filePath)) {
           if (fileReader.read() == -1) {
               return;
           } else {
               fileReader.close();
               JSONArray jsonArray = (JSONArray) parser.parse(new FileReader(filePath));

               System.out.println("---------------------------------------------------------------------------------------");
               System.out.println("|\t" + "\t\t  " + "\t\t\t\t");
               System.out.println("|\t" + "\t\t" + "Available Medications" + "\t\t");
               System.out.println("|\t" + "\t\t  " + "\t\t\t\t");
               System.out.println("---------------------------------------------------------------------------------------");
               System.out.println("| Medication ID |  Medication Name   |    Medication Price ||    Medication Quantity |");
               System.out.println("---------------------------------------------------------------------------------------");

               for (Object obj : jsonArray) {
                   JSONObject jsonObject = (JSONObject) obj;

                   // TODO: Add code to get medication ID (it's named as code from medications/products file), name, price and quantity
                   // medication ID, name, price and quantity should be casted to String
                   System.out.println("|\t" + jsonObject.get("code") + "\t\t" + jsonObject.get("name") + "\t\t\t" + jsonObject.get("price") + "\t\t\t" + jsonObject.get("quantity") + "\t\t\t");


               }
               System.out.println("---------------------------------------------------------------------------------------");

           }

       }
   }}
