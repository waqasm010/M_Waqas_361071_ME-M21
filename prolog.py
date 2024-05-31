# Define diseases and their symptoms
diseases = {
    "flu": ["fever", "headache", "fatigue", "sore_throat"],
    "cold": ["sneezing", "runny_nose", "sore_throat", "cough"],
    "covid19": ["fever", "dry_cough", "fatigue", "loss_of_taste_or_smell"],
    "malaria": ["fever", "chills", "sweating", "headache"],
    "dengue": ["fever", "headache", "joint_muscle_pain", "rash"]
}

def diagnose(disease):
    symptoms = diseases[disease]
    for symptom in symptoms:
        answer = input(f"Do you have {symptom}? (yes/no): ").strip().lower()
        if answer != "yes":
            return False
    return True

def start_diagnosis():
    disease = input("Which disease do you want to diagnose? (flu/cold/covid19/malaria/dengue): ").strip().lower()
    if disease in diseases:
        if diagnose(disease):
            print(f"You might have {disease}.")
        else:
            print("Diagnosis inconclusive.")
    else:
        print("Unknown disease.")

# Start the diagnosis process
if __name__ == "__main__":
    start_diagnosis()
