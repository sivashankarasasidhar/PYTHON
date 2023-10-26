
"""Q.Write a program to build a simple hospital management system using Python which can perform the following operations: 
1.write a method to takes details from the patient then store.
2.write a method to display all the details of patients.
3.write a method to search particular patient from the list. search by ID 
4.write a method to delete a particular patient details by ID.
5.write a method to update a selected patient details by ID.   
use list, dictionary to store data"""

class Patient:
    def __init__(self, patient_id, name, age, gender, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Diagnosis: {self.diagnosis}"

class Hospi_Mag_Sys:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient_id, name, age, gender, diagnosis):
        patient = Patient(patient_id, name, age, gender, diagnosis)
        self.patients.append(patient)
        print(f"Patient with ID {patient_id} added successfully.")

    def display_patients(self):
        print("Patient Details:")
        for patient in self.patients:
            print(patient)

    def search_patient(self, patient_id):
        found = False
        for patient in self.patients:
            if patient.patient_id == patient_id:
                print("Patient Found:")
                print(patient)
                found = True
                break
        if not found:
            print(f"Patient with ID {patient_id} not found.")

    def delete_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                print(f"Patient with ID {patient_id} deleted")
                return
        print(f"Patient with ID {patient_id} not found.")

    def update_patient(self, patient_id, updated_data):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                for key, value in updated_data.items():
                    setattr(patient, key, value)
                print(f"Patient with ID {patient_id} updated")
                return
        print(f"Patient with ID {patient_id} not found.")

def main():
    hospital = Hospi_Mag_Sys()

    while True:
        print("\nHospi_Mag_Sys")
        print("1. Add Patient")
        print("2. Dis_Patients")
        print("3. Search_Patient")
        print("4. Delete_Patient")
        print("5. Update_Patient")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            gender = input("Enter Patient Gender: ")
            diagnosis = input("Enter Patient Diagnosis: ")
            hospital.add_patient(patient_id, name, age, gender, diagnosis)
        elif choice == "2":
            hospital.display_patients()
        elif choice == "3":
            patient_id = input("Enter Patient ID to search: ")
            hospital.search_patient(patient_id)
        elif choice == "4":
            patient_id = input("Enter Patient ID to delete: ")
            hospital.delete_patient(patient_id)
        elif choice == "5":
            patient_id = input("Enter Patient ID to update: ")
            name = input("Enter Updated Name: ")
            age = input("Enter Updated Age: ")
            gender = input("Enter Updated Gender: ")
            diagnosis = input("Enter Updated Diagnosis: ")
            updated_data = {
                "name": name,
                "age": age,
                "gender": gender,
                "diagnosis": diagnosis,
            }
            hospital.update_patient(patient_id, updated_data)
        elif choice == "6":
            print("Exiting the Hospital")
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
