import openai
from fpdf import FPDF
from datetime import datetime
import locale

# Configurer la locale pour utiliser le français
locale.setlocale(locale.LC_TIME, 'fr_FR')

def select_job():
    jobs = ["Développeur logiciel", "Analyste programmeur", "Technicien de maintenance informatique", "Développeur Web", "Développeur back-end" ,"Concepteur développeur informatique"]
    print("Sélectionnez le métier pour votre lettre de motivation :") # peut changer en fonction du metier
    for i, job in enumerate(jobs):
        print(f"{i + 1}. {job}")
    choice = int(input("Entrez le numéro du métier : ")) - 1
    return jobs[choice]

def select_company():
    company_name = input("Entrez le nom de l'entreprise : ")
    return company_name

def generate_letter_content(company_name, position):
    openai.api_key = '' # a remplir 
    
    response = openai.ChatCompletion.create(
            model="gpt-4",
            messages= [{'role' : 'user' , 'content' :f"Générer une lettre de motivation sans l'en tete  pour le poste de {position} chez {company_name} pour une alternance pour mon bts sio option solutions logicielles et applications métiers avec pour objet ,OBJET : RECHERCHE D'ALTERNANCE POUR 1 OU 2 ANS. Mes competences en info sont : Python , SQL , PHP , css et HTML. et pour la signature  c'est EL ASSIR Rayan"}],
            max_tokens=1000
    )
    return response['choices'][0]['message']['content']
    

def create_custom_letter(company_name, position, your_name, your_address, your_email, your_phone):
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)  # intaller et mettre la police dans le meme dossier
    pdf.set_font('DejaVu', '', 11)
    pdf.set_margins(10, 10, 10)

    personal_info = f"{your_name}\n{your_address}\n{your_phone}\n{your_email}\n\n"
    pdf.multi_cell(0, 10, personal_info)

    today_date = datetime.now().strftime("%d %B %Y")
    pdf.cell(0, 10, today_date, ln=True, align="R")

    letter_content = generate_letter_content(company_name, position)
    pdf.multi_cell(0, 5, letter_content)
    pdf.output("custom_letter.pdf")

# Exemple d'utilisation
job_selected = select_job()
company_selected = select_company()
create_custom_letter(company_selected, job_selected, "EL ASSIR Rayan", 
                     "adresse", "elassir.rayan@gmail.com", "numero")