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


conn.commit()
conn.close()
print("setup complete!")
