import sqlite3
def get_data():
   conn = sqlite3.connect("database_tables_1.db")
   cursor = conn.cursor()

   cursor.execute("""

       SELECT
         disease_only.disease,
         symptoms_only.symptom,
         disease_symptom_combo.weight

       FROM disease_symptom_combo

       JOIN disease_only
       ON disease_symptom_combo.disease_id = disease_only.id

       JOIN symptoms_only
       ON disease_symptom_combo.symptoms_id = symptoms_only.id


         """)

   data = cursor.fetchall()

   conn.close()
   return data

def get_synonyms():

    conn = sqlite3.connect("database_tables_1.db")
    cursor = conn.cursor()

    cursor.execute("""

        SELECT
        synonym_part1.Reference,
        synonym_part2.Refered

        FROM part1_part2
        JOIN synonym_part1
        ON part1_part2.reference_id = synonym_part1.id

       JOIN synonym_part2
       ON part1_part2.refered_id = synonym_part2.id



         """)
    data2 = cursor.fetchall()

    conn.close()
    return data2


def incoming_disease(rows):

    diagnosis_dict = {}

    for disease, symptoms, weight in rows:
        if disease not in diagnosis_dict:
           diagnosis_dict[disease] = {}

        diagnosis_dict[disease][symptoms] = weight

    return diagnosis_dict


def incoming_synonyms(rows):

    diagnosis_symptoms = {}

    for symptom, synonym in rows:
        if symptom not in diagnosis_symptoms:
           diagnosis_symptoms[symptom] = []

        diagnosis_symptoms[symptom].append(synonym)

    return diagnosis_symptoms



mavalue = get_data()
diagnosis_symptoms = incoming_disease(mavalue)

mavalue2 = get_synonyms()
synonyms = incoming_synonyms(mavalue2)








user_symptoms = input("input symptoms separated by comas: ")
user_symptoms = [symptoms.strip().lower() for symptoms in user_symptoms.split(',')]

def diagnose(user_symptoms, diagnosis_symptoms, synonyms):

   highest_percentage = 0
   best_percentage = []

   for  diagnosis, symptoms in diagnosis_symptoms.items():

        score = 0
        max_score = sum(symptoms.values())

        if max_score == 0:
           continue

        for user_symptom in user_symptoms:

            for actual_symptoms, values in symptoms.items():

                if actual_symptoms in user_symptom or user_symptom in actual_symptoms:


                   score += values

                elif actual_symptoms in synonyms:

                     for synonym in  synonyms[actual_symptoms]:

                         if user_symptom in synonym or synonym in user_symptom:

                             score += values

        percentage = (score / max_score)*100

        if  percentage > highest_percentage:
              highest_percentage = percentage
              best_percentage = [diagnosis]

        elif percentage == highest_percentage:

             best_percentage.append(diagnosis)

   return best_percentage,highest_percentage

result = (diagnose(user_symptoms, diagnosis_symptoms, synonyms))
print(f"you are most likely suffering from: {result}")

