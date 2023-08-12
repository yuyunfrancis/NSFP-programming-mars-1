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

		public Prescription(String prescriptionID,String customerID, String doctorName, LocalDate dateToPrint, ArrayList<Medication> medications) {
		   this.prescriptionID = prescriptionID;
		   this.customerID = customerID;
		   this.doctorName = doctorName;
		   this.date = dateToPrint;
		   this.medications = medications;

		}


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
	   

		FileHandler fileHandler = new FileHandler();
	public void addPrescription() throws IOException, ParseException {
		JSONArray existingPrescriptions = fileHandler.readJSONArrayFromFile();
		JSONObject prescriptionObject = new JSONObject();

		prescriptionObject.put("DoctorName", this.getDoctorName());
		prescriptionObject.put("PrescriptionID", this.getPrescriptionID());
		prescriptionObject.put("Medications", getMedicationsOnPrescription(this));
		prescriptionObject.put("CustomerID", this.getCustomerID());
		prescriptionObject.put("Date", this.getDate().toString());

		existingPrescriptions.add(prescriptionObject);

		fileHandler.writeJSONArrayToFile(existingPrescriptions);
	}
	   
	   


		private JSONArray  getMedicationsOnPrescription(Prescription prescription) {
			JSONArray jsonArray = new JSONArray();

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


	   	public ArrayList<Prescription> viewPrescription() throws IOException, ParseException {

	        JSONArray jsonArray = fileHandler.readJSONArrayFromFile();



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
	   
	   


		public void deletePrescription(String prescrID) throws IOException, ParseException {
			JSONArray existingPrescriptions = fileHandler.readJSONArrayFromFile();
			int indexToDelete = -1;
			for (int i = 0; i < existingPrescriptions.size(); i++) {
				JSONObject jsonObject = (JSONObject) existingPrescriptions.get(i);
				String existingPrescriptionID = (String) jsonObject.get("PrescriptionID");


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

