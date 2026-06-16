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
        "image": supabase_img("cilios2"),
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
        "image": supabase_img("sobrancelha2"),
    },
    {
        "id": 6,
        "category": "sobrancelhas",
        "category_label": "Sobrancelhas",
        "name": "Design de sobrancelha com henna",
        "description": "Modelagem personalizada das sobrancelhas com o uso de henna para um resultado duradouro e natural.",
        "price": "R$ 50,00",
        "image": supabase_img("sobrancelha3"),
    },
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
    )

if __name__ == "__main__":
    app.run(debug=True)