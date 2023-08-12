public class Medication {

   private String ID;
   private String name;
   private String details;
   private String dosage;
   private int quantity;
   private Boolean processedStatus;

   public Medication() {
	   this.processedStatus = false;
   }

   public Medication(String _id,String _name,int qty ) {
      this.ID = _id;
      this.name =_name;
      this.quantity = qty;
      this.processedStatus = false;
   }

   // TODO: Add code to help you to create object/instance for this class in different way
   public Medication(String medicationID, String medicationName, String medicationDetails, String dosage, int quantity){
      this.ID = medicationID;
      this.name = medicationName;
      this.details = medicationDetails;
      this.dosage = dosage;
      this. quantity = quantity;
   }





   // TODO: Add code to help you to access or modify data members for this class
   public String getID() {
      return this.ID;
   }

   public String getName(){
      return this.name;
   }

   public String getDetails(){
      return this.details;
   }

   public String getDosage(){
      return this.dosage;
   }

   public int getQuantity(){
      return this.quantity;
   }

   public Boolean getProcessedStatus(){
      return this.processedStatus;
   }

   public void setID(String ID){
      this.ID = ID;
   }

   public void setName(String name){
      this.name = name;
   }

   public void setDetails(String details){
      this.details = details;
   }

   public void setQuantity(int quantity){
      this.quantity = quantity;
   }

   public void setDosage(String dosage){
      this.dosage = dosage;
   }




   public String toString() {
      return this.ID + "," + this.name + "," + this.quantity + "," + this.processedStatus;
   }
}