import sqlite3

conn = sqlite3.connect("database_tables_1.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS diseases_symptoms (

           id INTEGER PRIMARY KEY AUTOINCREMENT,
           disease TEXT,
           symptom TEXT,
           weight INTEGER

)
""")



diagnosis_symptoms = {

    "Flu": {
        "fever": 3,
        "body aches": 3,
        "fatigue": 2,
        "cough": 2,
        "sore throat": 1,
        "runny nose": 1
    },

    "Cold": {
        "runny nose": 3,
        "sneezing": 3,
        "sore throat": 2,
        "cough": 2,
        "mild headache": 1
    },

    "COVID-19": {
        "loss of taste/smell": 4,
        "shortness of breath": 3,
        "fever": 2,
        "cough": 2,
        "fatigue": 1,
        "sore throat": 1
    },

    "Asthma": {
        "wheezing": 4,
        "shortness of breath": 3,
        "chest tightness": 3,
        "coughing": 2
    },

        "Pneumonia": {
        "chills": 3,
        "chest pain": 3,
        "shortness of breath": 3,
        "fever": 2,
        "cough": 2,
        "fatigue": 1
    },

    "Migraine": {
        "severe headache": 4,
        "sensitivity to light": 3,
        "sensitivity to sound": 3,
        "nausea": 2,
        "vomiting": 2
    },

    "Diabetes": {
        "frequent urination": 4,
        "increased thirst": 4,
        "unexplained weight loss": 3,
        "blurred vision": 2,
        "fatigue": 1
    },

    "Hypertension": {
        "chest pain": 3,
        "shortness of breath": 2,
        "dizziness": 2,
        "headaches": 1
    },

        "Hypertension": {
        "chest pain": 3,
        "shortness of breath": 2,
        "dizziness": 2,
        "headaches": 1
    },

    "Gastritis": {
        "stomach pain": 3,
        "nausea": 2,
        "vomiting": 2,
        "loss of appetite": 2,
        "bloating": 1
    },

    "Anxiety": {
        "rapid heartbeat": 3,
        "restlessness": 2,
        "sweating": 2,
        "trouble concentrating": 2,
        "irritability": 2,
        "fatigue": 1
    }

}

synonyms = {

    "fever": [
        "high temperature",
        "hot body",
        "burning up",
        "temperature"
    ],

    "cough": [
        "coughing",
        "persistent cough",
        "dry cough",
        "wet cough"
    ],

    "fatigue": [
        "tired",
        "exhausted",
        "low energy",
        "weak",
        "feeling tired"
    ],

        "runny nose": [
        "stuffy nose",
        "blocked nose",
        "nasal discharge",
        "dripping nose"
    ],

    "sore throat": [
        "throat pain",
        "painful throat",
        "scratchy throat",
        "throat irritation"
    ],

    "headache": [
        "head pain",
        "migraine",
        "pressure in head",
        "aching head"
    ],

    "shortness of breath": [
        "difficulty breathing",
        "breathlessness",
        "hard to breathe",
        "can't breathe well"
    ],

    "nausea": [
        "feeling sick",
        "queasy",
        "upset stomach",
        "want to vomit"
    ],

       "vomiting": [
        "throwing up",
        "puking",
        "being sick",
        "vomit"
    ],

    "diarrhea": [
        "loose stool",
        "watery stool",
        "frequent stool",
        "runny stomach"
    ],

    "body aches": [
        "body pain",
        "muscle pain",
        "aching body",
        "sore muscles"
    ],

    "chills": [
        "shivering",
        "feeling cold",
        "cold shivers"
    ],

    "loss of taste": [
        "can't taste",
        "no taste",
        "taste loss"
    ],

        "loss of smell": [
        "can't smell",
        "no smell",
        "smell loss"
    ]
}






disease_data = []

for magonjwa in diagnosis_symptoms:

     madalili = diagnosis_symptoms[magonjwa]

     for dalili in madalili:

        uzito = madalili[dalili]

        disease_data.append((magonjwa, dalili, uzito))



cursor.executemany("INSERT INTO diseases_symptoms (disease, symptom, weight) VALUES (?,?,?)", disease_data)

cursor.execute("""CREATE TABLE IF NOT EXISTS symptoms_synonym (

           id INTEGER PRIMARY KEY AUTOINCREMENT,
           symptom TEXT,
           synonym TEXT

)
""")

symptom_data = []
for symptoms in synonyms:
    synonym = synonyms[symptoms]

    for syno in synonym:
        symptom_data.append((symptoms, syno))

cursor.executemany("INSERT INTO symptoms_synonym (symptom, synonym) VALUES (?,?)", symptom_data)


disease_only_list = []
for diseases_only in diagnosis_symptoms:
    disease_only_list.append((diseases_only,))

symptoms_only_list = []
for diseasess, symptoms_only in diagnosis_symptoms.items():
     for symptom_only in symptoms_only:
          symptoms_only_list.append((symptom_only,))



cursor.execute("""CREATE TABLE IF NOT EXISTS disease_only (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease TEXT
)
""")

cursor.executemany("INSERT INTO disease_only (disease) VALUES(?)", disease_only_list)


cursor.execute("""CREATE TABLE IF NOT EXISTS symptoms_only (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       symptom TEXT

)
""")


cursor.executemany("INSERT INTO symptoms_only (symptom) VALUES(?)", symptoms_only_list)


cursor.execute("SELECT id, disease FROM disease_only")

disease_lookup = {}

for disease_id, disease_name in cursor.fetchall():
    disease_lookup[disease_name] = disease_id 

cursor.execute("SELECT id, symptom FROM symptoms_only")

symptoms_lookup = {}

for symptoms_id, symptoms_name in cursor.fetchall():
    symptoms_lookup[symptoms_name] = symptoms_id

combo_data = []

for disease_name in diagnosis_symptoms:
    disease_id = disease_lookup[disease_name]
    symptoms = diagnosis_symptoms[disease_name]

    for symptoms_name in symptoms:
        symptoms_id = symptoms_lookup[symptoms_name]
        weight = symptoms[symptoms_name]

        combo_data.append(
                     (disease_id, symptoms_id, weight)

                    )




cursor.execute("""CREATE TABLE IF NOT EXISTS disease_symptom_combo (

           id INTEGER PRIMARY KEY AUTOINCREMENT,
           disease_id INTEGER NOT NULL,
           symptoms_id INTEGER NOT NULL,
           weight INTEGER NOT NULL,

          FOREIGN KEY(disease_id) REFERENCES disease(id),
          FOREIGN KEY(symptoms_id) REFERENCES symptom(id)

)
""")

cursor.executemany("INSERT INTO disease_symptom_combo (disease_id, symptoms_id, weight) VALUES(?,?,?)", combo_data)

reference_holder = []
for reference in synonyms:
    reference_holder.append((reference,))

cursor.execute("""CREATE TABLE IF NOT EXISTS synonym_part1 (

           id INTEGER PRIMARY KEY AUTOINCREMENT,
           Reference TEXT

)""")


cursor.executemany("INSERT INTO synonym_part1 (Reference) VALUES (?)", reference_holder)

refered_holder = []
for refer, refered in synonyms.items():
    for alternatives in refered:
        refered_holder.append((alternatives,))

cursor.execute("""CREATE TABLE IF NOT EXISTS synonym_part2(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Refered TEXT

)""")

cursor.executemany("INSERT INTO synonym_part2 (Refered) VALUES (?)", refered_holder)

cursor.execute("""CREATE TABLE IF NOT EXISTS part1_part2 (

           id INTEGER PRIMARY KEY AUTOINCREMENT,
           reference_id INTEGER NOT NULL,
           refered_id INTEGER NOT NULL,

         FOREIGN KEY(reference_id) REFERENCES Reference(id)
         FOREIGN KEY(refered_id)  REFERENCES Refered(id)
)""")


combo_list_synonyms = []
cursor.execute("SELECT id, Reference FROM synonym_part1")

reference_lookup = {}

for ref_id, ref_name in cursor.fetchall():
    reference_lookup[ref_name] = ref_id

cursor.execute("SELECT id, Refered FROM synonym_part2")

refered_lookup = {}

for red_id, red_name in cursor.fetchall():
    refered_lookup[red_name] = red_id

for res_diagnosis in synonyms:

     synonymsss = synonyms[res_diagnosis]

     ref_id = reference_lookup[res_diagnosis]

     for synonymses in synonymsss:
         red_id = refered_lookup[synonymses]

         combo_list_synonyms.append(

                 (ref_id, red_id)
               )

cursor.executemany("INSERT INTO part1_part2 (reference_id, refered_id) VALUES (?,?)", combo_list_synonyms)

conn.commit()
conn.close()
print("setup complete")
