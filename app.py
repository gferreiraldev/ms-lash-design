import os
from flask import Flask, render_template
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

app = Flask(__name__)

# --- Configuration ---
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")

def supabase_img(filename):
    base_url = SUPABASE_URL.strip().replace("/rest/v1/", "").rstrip('/')
    
    if "." not in filename:
        filename += ".jpeg"
        
    safe_filename = filename.replace(" ", "%20")
    
    return f"{base_url}/storage/v1/object/public/{SUPABASE_BUCKET}/{safe_filename}"

# --- Data (would come from PostgreSQL in production) ---
SERVICES = [
    # Cílios
    {
        "id": 1,
        "category": "cilios",
        "category_label": "Cílios",
        "name": "Fox eyes/cílios gatinho",
        "description": "Técnica que alonga os cílios externos, criando um efeito felino e sofisticado, perfeito para realçar o olhar.",
        "price": "R$ 160,00",
        "image": supabase_img("cilios1"),
    },
    {
        "id": 2,
        "category": "cilios",
        "category_label": "Cílios",
        "name": "Volume Glamour 5D",
        "description": "Técnica de volume extremo que proporciona um efeito dramático, com cílios densos e volumosos para um olhar marcante e impactante.",
        "price": "R$ 160,00",
        "image": supabase_img("cilios22"),
    },
    {
        "id": 3,
        "category": "cilios",
        "category_label": "Cílios",
        "name": "Volume Brasileiro",
        "description": "Técnica de volume que cria um efeito mais natural, com cílios levemente mais densos e alongados, ideal para realçar a beleza natural do olhar.",
        "price": "R$ 130,00",
        "image": supabase_img("cilios3"),
    },
    {
        "id": 7,
        "category": "cilios",
        "category_label": "Cílios",
        "name": "Volume power 3D",
        "description": "Técnica de volume que proporciona um efeito mais intenso e marcante, com cílios densos e alongados, ideal para quem deseja um olhar poderoso e impactante.",
        "price": "R$ 160,00",
        "image": supabase_img("cilios77"),
    },
    {
        "id": 8,
        "category": "cilios",
        "category_label": "Cílios",
        "name": "Volume Egípcio",
        "description": "Técnica de volume que cria um efeito mais dramático e marcante, com cílios densos e alongados, ideal para realçar a beleza do olhar e criar um visual sofisticado.",
        "price": "R$ 140,00",
        "image": supabase_img("cilios8"),
    },
    {
        "id": 9,
        "category": "cilios",
        "category_label": "Cílios",
        "name": "Efeito rimel/molhado",
        "description": "Técnica que proporciona um efeito de cílios molhados, com fios mais curvados e alongados, criando um visual moderno e elegante, perfeito para realçar o olhar de forma sutil e sofisticada.",
        "price": "R$ 140,00",
        "image": supabase_img("cilios99"),
    },
    {
        "id": 12,
        "category": "cilios",
        "category_label": "Cílios",
        "name": "Lash lifting",
        "description": "Técnica que eleva e define os cílios, criando um efeito mais longo e volumoso, ideal para realçar o olhar de forma natural e duradoura.",
        "price": "R$ 100,00",
        "image": supabase_img("cilios122"),
    },
    {
        "id": 11,
        "category": "cilios",
        "category_label": "Cílios",
        "name": "Remoção Química de Extensão de Cílios",
        "description": "Técnica que utiliza produtos específicos para remover a extensão de cílios de forma segura e eficaz, sem danificar os cílios naturais, proporcionando um processo de remoção suave e confortável.",
        "price": "R$ 30,00",
        "image": supabase_img("cilios11"),
    },
    {
        "id": 13,
        "category": "cilios",
        "category_label": "Cílios",
        "name": "Volume moana",
        "description": "entrega um olhar marcante, elegante e cheio de movimento. Com fios bem alinhados e um acabamento sofisticado, proporciona um efeito de rímel intenso sem perder a delicadeza, valorizando a beleza natural de cada olhar.",
        "price": "R$ 140,00",
        "image": supabase_img("cilios13"),
    },
    # Sobrancelhas
    {
        "id": 4,
        "category": "sobrancelhas",
        "category_label": "Sobrancelhas",
        "name": "Brow Lamination",
        "description": "Técnica que alinha e fixa os fios das sobrancelhas para um resultado mais definido e natural.",
        "price": "R$ 90,00",
        "image": supabase_img("sobrancelha1"),
    },
    {
        "id": 5,
        "category": "sobrancelhas",
        "category_label": "Sobrancelhas",
        "name": "Design de sobrancelha",
        "description": "Modelagem personalizada das sobrancelhas, utilizando técnicas de depilação e design para realçar a beleza natural do rosto.",
        "price": "R$ 40,00",
        "image": supabase_img("sobrancelha22"),
    },
    {
        "id": 6,
        "category": "sobrancelhas",
        "category_label": "Sobrancelhas",
        "name": "Design de sobrancelha com henna",
        "description": "Modelagem personalizada das sobrancelhas com o uso de henna para um resultado duradouro e natural.",
        "price": "R$ 50,00",
        "image": supabase_img("sobrancelha33"),
    },
    {
        "id": 10,
        "category": "depilacao",
        "category_label": "Depilação",
        "name": "Depilação de buço com cera",
        "description": "Técnica de depilação facial utilizando cera para remover pelos indesejados, proporcionando uma pele lisa e suave.",
        "price": "R$ 12,00",
        "image": supabase_img("depilacao1"),
    }
]

TESTIMONIALS = [
    {
        "name": "Ana Paula",
        "text": "Amei o resultado! Meus cílios ficaram perfeitos, super naturais e duradouros. Recomendo demais! 😍",
        
    },
    {
        "name": "Juliana M.",
        "text": "Atendimento impecável, ambiente lindo e o resultado superou minhas expectativas! Já marquei a manutenção. ✨",
        
    },
    {
        "name": "Fernanda R.",
        "text": "Melhor investimento que fiz! Acordo linda todo dia sem precisar de maquiagem nos olhos. 💛",
        
    },
    {
        "name": "Camila S.",
        "text": "O design de sobrancelha mudou meu rosto! Carinhosa, caprichosa e muito profissional. Nota 10! 🌟",
        
    },
    {
        "name": "Larissa T.",
        "text": "Primeira vez fazendo extensão e me apaixonei! Técnica incrível, resultado deslumbrante. Voltarei sempre! 💫",
        
    },
]

PORTFOLIO_IMAGES = [
    supabase_img("lashes1"),
    supabase_img("lashes2"),
    supabase_img("lashes3"),
    supabase_img("lashes4"),
    supabase_img("lashes5"),
    supabase_img("lashes6")
]

@app.route("/")
def index():
    return render_template(
        "index.html",
        services=SERVICES,
        testimonials=TESTIMONIALS,
        portfolio_images=PORTFOLIO_IMAGES,
        supabase_logo=supabase_img("image_ddfe48.png"),
        supabase_biografia=supabase_img("biografia"),
    )

if __name__ == "__main__":
    app.run(debug=True)