import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Objects;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


public class Prescription {
	   private String prescriptionID;
	   private String customerID;
	   private String doctorName;
	   private ArrayList<Medication> medications;
	   private LocalDate date;
	   private static JSONArray prescriptionList;
	   

	   public Prescription() { 
		   prescriptionList = new JSONArray();
	   }
	   
	   public Prescription(String _prescriptionID, String _customerID, String _doctorName, ArrayList<Medication> _medication)
	   {
	       prescriptionID = _prescriptionID;
	       customerID = _customerID;
	       doctorName = _doctorName;
	       medications = _medication;
	       date = LocalDate.now();

	   }
	  
   // TODO: Add code to help you to create object/instance for this class in different way
		public Prescription(String prescriptionID,String customerID, String doctorName, LocalDate dateToPrint, ArrayList<Medication> medications) {
		   this.prescriptionID = prescriptionID;
		   this.customerID = customerID;
		   this.doctorName = doctorName;
		   this.date = dateToPrint;
		   this.medications = medications;

		}






	    // TODO: Add code to help you to access or modify data members for this class
	   public String getPrescriptionID() {
		   return this.prescriptionID;
	   }

	   public String getCustomerID() {
		   return this.customerID;
	   }

	   public String getDoctorName() {
		   return this.doctorName;
	   }

	   public LocalDate getDate(){
		   return this.date;
	   }

	   public ArrayList<Medication> getMedications() {
		   return this.medications;
	   }

	   public JSONArray getPrescriptionList() {
		   return prescriptionList;
	   }

	   public void setPrescriptionID(String prescriptionID) {
		   this.prescriptionID = prescriptionID;
	   }

	   public void setCustomerID(String customerID) {
		   this.customerID = customerID;
	   }

	   public void setDoctorName(String doctorName) {
		   this.doctorName = doctorName;
	   }

	   public void setMedications(ArrayList<Medication> medications){
		   this.medications = medications;
	   }

	   public void setDate(LocalDate date){
		   this.date = date;
	   }
	   



		// TODO: Add code needed to be able to add prescription in the file
		// While adding the prescription in the file, please follow the format shown below
		// Format for the prescription: {"DoctorName":"Yves","PrescriptionID":"TA3","Medications":[{"quantity":2,"processedStatus":false,"name":"IBUPROFEN","id":"IB7"}],"CustomerID":"GR","Date":"2023-08-07"}
		FileHandler fileHandler = new FileHandler();
	public void addPrescription() throws IOException, ParseException {
		JSONArray existingPrescriptions = fileHandler.readJSONArrayFromFile();
		JSONObject prescriptionObject = new JSONObject();

		// TODO: Add code to add prescription in the file
		prescriptionObject.put("DoctorName", this.getDoctorName());
		prescriptionObject.put("PrescriptionID", this.getPrescriptionID());
		prescriptionObject.put("Medications", getMedicationsOnPrescription(this));
		prescriptionObject.put("CustomerID", this.getCustomerID());
		prescriptionObject.put("Date", this.getDate().toString());

		existingPrescriptions.add(prescriptionObject);

		fileHandler.writeJSONArrayToFile(existingPrescriptions);
	}
	   
	   
	   
		// TODO: Add code needed to be able to get all medications on the prescription  
		// TODO: You must return an array of medications!

		private JSONArray  getMedicationsOnPrescription(Prescription prescription) {
			JSONArray jsonArray = new JSONArray();

			// TODO: Add code to get medications on the prescription
			ArrayList<Medication> medications = prescription.getMedications();
            for (Medication medication : medications) {
                JSONObject medObj = new JSONObject();
                medObj.put("name", medication.getName());
                medObj.put("id", medication.getID());
                medObj.put("quantity", medication.getQuantity());
                medObj.put("processedStatus", medication.getProcessedStatus());
                jsonArray.add(medObj);
            }
			return jsonArray;

        }
	    
	   
		// TODO: Add code to help you viewing all prescriptions in the file
		// You must return an array of prescriptions

	   	public ArrayList<Prescription> viewPrescription() throws IOException, ParseException {
			// TODO: Add code to help you reading from the prescriptions.json file

	        JSONArray jsonArray = fileHandler.readJSONArrayFromFile();


	        // TODO: Add code to help you creating an array of prescriptions

			ArrayList<Prescription> prescriptions = new ArrayList<Prescription>();

	        for (Object obj : jsonArray) {
	            JSONObject jsonObject = (JSONObject) obj;
                
                String doctorName = (String) jsonObject.get("DoctorName");
                String prescriptionID = (String) jsonObject.get("PrescriptionID");
                String customerID = (String) jsonObject.get("CustomerID");
                String date = (String) jsonObject.get("Date");
                LocalDate dateToPrint = LocalDate.parse(date);
                
                ArrayList<Medication> medications = new ArrayList<Medication>();
                
                JSONArray medicationsArray = (JSONArray) jsonObject.get("Medications");

                for (Object medObj : medicationsArray) {
                    JSONObject medication = (JSONObject) medObj;

					// TODO: Add code to get medication ID, name and quantity
					// medication quantity should be casted to int
                    // also medication ID and name should be casted to String
					String medicationID = (String) medication.get("id");
					String medicationName = (String) medication.get("name");
					Long amount = (Long) medication.get("quantity");
					int quantity = amount.intValue();


                    medications.add(new Medication(medicationID, medicationName, quantity));
                }

                prescriptions.add(new Prescription(prescriptionID,customerID, doctorName, dateToPrint, medications));
            }
			return prescriptions;
	    }
	   
	   


		// TODO: Add code to help you deleting a specific prescription
		public void deletePrescription(String prescrID) throws IOException, ParseException {
			// TODO: Add code to help you reading from the prescriptions.json file
			JSONArray existingPrescriptions = fileHandler.readJSONArrayFromFile();

			int indexToDelete = -1;
			for (int i = 0; i < existingPrescriptions.size(); i++) {
				JSONObject jsonObject = (JSONObject) existingPrescriptions.get(i);
				String existingPrescriptionID = (String) jsonObject.get("PrescriptionID");

				// TODO: Add code to check if the prescription you want to delete is similar to one exists
				if (Objects.equals(existingPrescriptionID, prescrID)) {
					indexToDelete = i;
					break;
				}
			}

			if (indexToDelete != -1) {
				existingPrescriptions.remove(indexToDelete);
				fileHandler.writeJSONArrayToFile(existingPrescriptions);
			}
		}
			
}

