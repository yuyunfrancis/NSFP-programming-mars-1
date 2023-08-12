import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import org.json.simple.parser.ParseException;


public class Prescription {
	   private String prescriptionID;
	   private String customerID;
	   private String doctorName;
	   private ArrayList<Medication> medications;
	   private LocalDate date;
	   private static JSONArray prescriptionList;
	   private FileHandler fileHandler;


	public Prescription() {
		   prescriptionList = new JSONArray();fileHandler = new FileHandler();
	   }
	   
	   public Prescription(String _prescriptionID, String _customerID, String _doctorName, ArrayList<Medication> _medication)
	   {
	       prescriptionID = _prescriptionID;
	       customerID = _customerID;
	       doctorName = _doctorName;
	       medications = _medication;
	       date = LocalDate.now();
		   fileHandler = new FileHandler();
	   }

	public Prescription(String prescriptionID, String customerID, String doctorName, ArrayList<Medication> medications, LocalDate dateToPrint) {
		this.prescriptionID = prescriptionID;
		this.customerID = customerID;
		this.doctorName = doctorName;
		this.medications = medications;
		this.date = dateToPrint;
		fileHandler = new FileHandler();
	}
	    public void addPrescription() throws IOException, ParseException {
			JSONArray existingPrescriptions = fileHandler.readJSONArrayFromFile(true);
			existingPrescriptions.add(new Prescription(prescriptionID, customerID, doctorName, medications).getJSONObject());

			fileHandler.writeJSONArrayToFile(existingPrescriptions);
	    }

	private JSONObject getJSONObject() {
		JSONObject jsonObject = new JSONObject();
		jsonObject.put("DoctorName", doctorName);
		jsonObject.put("PrescriptionID", prescriptionID);
		jsonObject.put("CustomerID", customerID);

		JSONArray medicationsArray = new JSONArray();
		for (Medication medication : medications) {
			JSONObject medicationObject = new JSONObject();
			medicationObject.put("id", medication.getID());
			medicationObject.put("name", medication.getName());
			medicationObject.put("quantity", medication.getQuantity());
			medicationObject.put("processedStatus", medication.getProcessedStatus());
			medicationsArray.add(medicationObject);
		}
		jsonObject.put("Medications", medicationsArray);
		jsonObject.put("Date", date.toString());

		return jsonObject;
	}


	// TODO: Add code needed to be able to get all medications on the prescription
		// TODO: You must return an array of medications!


	public JSONArray  getMedicationsOnPrescription(Prescription prescription) throws IOException, ParseException {
		JSONArray jsonArray = new JSONArray();

		try {
			JSONArray existingPrescriptions = fileHandler.readJSONArrayFromFile(true);
            for (Object existingPrescription : existingPrescriptions) {
                JSONObject prescriptionObject = (JSONObject) existingPrescription;
                String existingPrescriptionID = (String) prescriptionObject.get("PrescriptionID");
                if (existingPrescriptionID.equals(prescription.getPrescriptionID())) {
                    jsonArray = (JSONArray) prescriptionObject.get("Medications");
                }
            }
		}catch (Exception e) {
			System.out.println("Error: " + e);
		}
        return jsonArray;
    }
	    
	   
		// TODO: Add code to help you viewing all prescriptions in the file
		// You must return an array of prescriptions

	   	public ArrayList<Prescription> viewPrescription() throws IOException, ParseException {
			// TODO: Add code to help you reading from the prescriptions.json file

	        JSONArray jsonArray = fileHandler.readJSONArrayFromFile(true);

			ArrayList<Prescription> prescriptions = new ArrayList<>();

	        for (Object obj : jsonArray) {
	            JSONObject jsonObject = (JSONObject) obj;
                
                String doctorName = (String) jsonObject.get("DoctorName");
                String prescriptionID = (String) jsonObject.get("PrescriptionID");
                String customerID = (String) jsonObject.get("CustomerID");
                String date = (String) jsonObject.get("Date");
                LocalDate dateToPrint = LocalDate.parse(date);
                
                ArrayList<Medication> medications = new ArrayList<>();
                
                JSONArray medicationsArray = (JSONArray) jsonObject.get("Medications");

                for (Object medObj : medicationsArray) {
                    JSONObject medication = (JSONObject) medObj;
					int quantity = (int) (long) medication.get("quantity");
					String medicationName = (String) medication.get("name");
					String medicationID = (String) medication.get("id");

					// TODO: Add code to get medication ID, name and quantity
					// medication quantity should be casted to int
                    // also medication ID and name should be casted to String

                    medications.add(new Medication(medicationID, medicationName, quantity));
                }

                prescriptions.add(new Prescription(prescriptionID, customerID, doctorName, medications, dateToPrint));
                
            }
			return prescriptions;

	    }
	   
	   


		// TODO: Add code to help you deleting a specific prescription
		public void deletePrescription(String prescrID) throws IOException, ParseException {
			// TODO: Add code to help you reading from the prescriptions.json file
			JSONArray existingPrescriptions = fileHandler.readJSONArrayFromFile(true);
			JSONArray newPrescriptions = new JSONArray();

			int indexToDelete = -1;
			for (int i = 0; i < existingPrescriptions.size(); i++) {
				JSONObject jsonObject = (JSONObject) existingPrescriptions.get(i);
				String existingPrescriptionID = (String) jsonObject.get("PrescriptionID");

				// TODO: Add code to check if the prescription you want to delete is similar to one exists
				if (existingPrescriptionID.equals(prescriptionID)) {
					indexToDelete = i;
					break;
				}
			}

			if (indexToDelete != -1) {
				existingPrescriptions.remove(indexToDelete);
				fileHandler.writeJSONArrayToFile(existingPrescriptions);
			}
		}

	public String getPrescriptionID() {
		return prescriptionID;
	}

	public void setPrescriptionID(String prescriptionID) {
		this.prescriptionID = prescriptionID;
	}

	public String getCustomerID() {
		return customerID;
	}

	public void setCustomerID(String customerID) {
		this.customerID = customerID;
	}

	public String getDoctorName() {
		return doctorName;
	}

	public void setDoctorName(String doctorName) {
		this.doctorName = doctorName;
	}

	public ArrayList<Medication> getMedications() {
		return medications;
	}

	public void setMedications(ArrayList<Medication> medications) {
		this.medications = medications;
	}

	public LocalDate getDate() {
		return date;
	}

	public void setDate(LocalDate date) {
		this.date = date;
	}

	public static JSONArray getPrescriptionList() {
		return prescriptionList;
	}

	public static void setPrescriptionList(JSONArray prescriptionList) {
		Prescription.prescriptionList = prescriptionList;
	}
}

