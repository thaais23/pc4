import streamlit as st
import random

st.set_page_config(layout="wide", page_title="Portafolio de Thais Choque")

# Estilos personalizados
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #fdf1f1;
        color: #2e2e2e;
        font-family: 'Georgia', serif;
    }
    h1, h2, h3 {
        color: #772f40;
    }
    .stTabs [role="tablist"] {
        justify-content: center;
    }
    .stButton button {
        background-color: #772f40;
        color: white;
        border-radius: 5px;
    }
    .vertical-line {
        border-left: 2px solid #d9a0a0;
        height: 100%;
        margin-left: 1rem;
        margin-right: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Frase aleatoria
frase = random.choice([
    "“Lo más importante no es la cámara, sino el ojo.” – Alfred Eisenstaedt",
    "“Cada plano es una emoción esperando ser descubierta.”",
    "“El cine también es una forma de escuchar.”",
    "“La sensibilidad guía la mirada.”"
])

# Crear estructura principal
col1, col_div, col2 = st.columns([1.2, 0.02, 3], gap="small")

# Columna izquierda (franja)
with col1:
    st.image("mi_foto_circular.png", width=180)
    st.markdown("<h2 style='color:#772f40;'>Thais Choque</h2>", unsafe_allow_html=True)
    st.markdown("Estudiante de Comunicación Audiovisual en la PUCP 🎬")
    st.markdown(f"<hr><em style='color:#555;'>{frase}</em><hr>", unsafe_allow_html=True)
    st.markdown("📫 <strong>Contacto:</strong><br>thaisgchoque@gmail.com", unsafe_allow_html=True)
    st.text_input("¿Te gustaría que te escriba de vuelta?", placeholder="Tu correo o red social")

# Columna intermedia: línea vertical separadora
with col_div:
    st.markdown("<div class='vertical-line'></div>", unsafe_allow_html=True)

# Columna derecha (contenido del portafolio)
with col2:
    tabs = st.tabs([
        "Inicio", 
        "Resume", 
        "Exploraciones Creativas", 
        "Research", 
        "Hobbies", 
        "Contacto"
    ])

    with tabs[0]:
        st.subheader("Inicio")
        st.markdown("""
Bienvenida a mi portafolio personal 🌷  
Aquí comparto mi proceso como estudiante de Comunicación Audiovisual, desde lo académico hasta lo que me inspira creativamente.
        """)

    with tabs[1]:
        st.subheader("Perfil Académico")
        st.markdown("""
**Formación**  
- Comunicación Audiovisual en la PUCP (5to ciclo)  
- Cursos centrados en narrativa visual, lenguaje audiovisual, fotografía y edición  

**Habilidades**  
- Edición básica de video  
- Fotografía y composición  
- Trabajo colaborativo y planificación  
- Curiosidad constante por nuevas herramientas digitales  

**Idiomas**  
- Español (nativo)  
- Inglés (avanzado)
        """)

    with tabs[2]:
        st.subheader("Exploraciones Creativas")
        st.markdown("""
**Ejercicios fotográficos**  
He trabajado con luz natural, retratos y composición. Me interesa cómo una imagen puede transmitir atmósferas.

**Análisis visual**  
Observar planos y el ritmo narrativo son claves para enriquecer mi comprensión del lenguaje cinematográfico.

**Trabajo colaborativo**  
He participado en procesos grupales de escritura y planificación visual. Valoro la creación colectiva desde distintas perspectivas.
        """)

    with tabs[3]:
        st.subheader("Líneas de Interés")
        st.markdown("""
- Representación de lo cotidiano en el cine y las series  
- Personajes femeninos en narrativas visuales  
- Estética digital en redes sociales  
- Impacto emocional del lenguaje audiovisual  
- Colores, texturas y silencios 
        """)

    with tabs[4]:
        st.subheader("Gustos e Inspiraciones")
        st.markdown("""
- Escuchar música: K-pop, Taylor Swift u otros artistas de pop 
- Ver k-dramas     
- Pasar tiempo con mi mascota Maya 🐾  
        """)

    with tabs[5]:
        st.subheader("Contacto")
        st.markdown("Puedes escribirme a:  \n📬 **thaisgchoque@gmail.com**")
        mensaje = st.text_area("💌 ¿Hay algo que quieras decirme?")
        if mensaje:
            st.success("¡Gracias por compartir tus palabras conmigo! ✨")
