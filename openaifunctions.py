import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
def config_api():
    load_dotenv()

config_api()
ghost = os.getenv("API_KEY")
client = OpenAI(api_key=ghost)


# Function to generate text using OpenAI
def generate_text(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
        {"role": "system", "content": "Du är en näringslivsexpert som förklarar kompetenser och fokuserar på dess användningsområden i näringslivet och hur den appliceras i organisationer."},
        {"role": "system", "content": "Du är pedagosisk och anger rubriker till varje stycke i versaler och skriv inte med några asterix tecken."},
        #{skriv en negativ prompt till systemet}
        {"role": "user", "content": "Skriv en strukturerad text som först förklarar kompetensen " + prompt +"."},

        {"role": "user", "content": "Förklara vilka andra kompetenser som ofta kombineras ihop med " + prompt + ". Förklara även vikten av sambandet mellan dessa kompetenser i arbetslivet."},
        {"role": "user", "content": "Förklara kort vilka sorters utbildningar som lär ut kompetensen."}
            ]
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        return f"An error occurred: {str(e)}"


"""
########################-------STREAMLIT--------##########################
import streamlit as st
#DATA
# Load data from CSV files and store them in a dictionary
data_by_year = {}
for year in range(2018, 2023):
    file_path = f"./CSVfiler/skills_by_occupation_update{year}.csv"
    try:
        data = pd.read_csv(file_path)
        file_year = re.search(r'\d{4}', file_path).group()
        data['Year'] = int(file_year)
        data_by_year[year] = data
    except FileNotFoundError:
        st.error(f"Data for year {year} not found.")




# Get all unique competencies from the data
all_competencies = set()
for data in data_by_year.values():
    all_competencies.update(data['Skill'].unique())


#HUVUDKOD/Visualiseringen
# Streamlit-app titel
st.title("Generera text om kompetenser")


# Dropdown menu for selecting competence
selected_competence = st.selectbox("Välj en kompetens", list(all_competencies))


# Generera och visa text när användaren klickar på knappen
if st.button("Generera text"):
    prompt = selected_competence #om jag vill ändra selected competence till en lista 
    generated_text = generate_text(prompt)
    st.text_area("Genererad text", generated_text)
"""