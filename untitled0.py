import streamlit as st

# Configuración general
st.set_page_config(page_title="Portafolio de Thais Choque", layout="wide")

# Estilos personalizados
st.markdown("""
    <style>
    /* Fondo crema rosado */
    html, body, [class*="css"] {
        background-color: #fdf1f1;
        color: #2e2e2e;
        font-family: 'Georgia', serif;
    }

    .stApp {
        background-color: #fdf1f1 !important;
        padding: 2rem;
    }

    /* Títulos en borgoña */
    h1, h2, h3 {
        color: #772f40 !important;
        font-weight: bold;
    }

    /* Inputs y botones */
    .stTextInput > div > div > input {
        color: #2e2e2e !important;
        background-color: #fff8f8 !important;
    }

    .stButton button {
        background-color: #772f40;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5em 1em;
    }

    </style>
""", unsafe_allow_html=True)

# Título + imagen circular + frase inspiradora en dos columnas
st.markdown("<h1 style='text-align: center;'>Portafolio de Thais Choque</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.image("mi_foto_circular.png", caption="Thais Choque", width=200)
with col2:
    st.markdown("""
    <div style="margin-top: 2rem;">
    <em style='font-size: 18px; color: #772f40;'>
    “Lo más importante no es la cámara, sino el ojo.”  
    </em><br>
    <span style='color:#444;'>— Alfred Eisenstaedt</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### Estudiante de Comunicación Audiovisual · PUCP")
st.write("Este portafolio reúne aspectos de mi formación, intereses creativos y sensibilidad visual en desarrollo.")

# Tabs de navegación
tabs = st.tabs([
    "Inicio", "Resume", "Exploraciones Creativas", "Research", "Achievements", "Hobbies", "Contacto"
])

with tabs[0]:
    st.subheader("Inicio")
    st.markdown("""
Bienvenida a mi portafolio personal.  
Aquí comparto mi proceso como estudiante de Comunicación Audiovisual, desde lo académico hasta lo que me inspira creativamente.

Cada sección refleja una parte distinta de mi formación y mis intereses.  
Gracias por estar aquí.
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
He trabajado con luz natural, retratos y composición. Me interesa cómo una imagen puede transmitir atmósferas sutiles.

**Análisis visual**  
Observar planos, ritmo narrativo y silencios significativos ha sido clave para enriquecer mi comprensión del lenguaje cinematográfico.

**Trabajo colaborativo**  
He participado en procesos grupales de escritura y planificación visual. Valoro la creación colectiva desde distintas perspectivas.
""")

with tabs[3]:
    st.subheader("Líneas de Interés")
    st.markdown("""
Temas que me interesan actualmente:

- Representación de lo cotidiano en el cine y las series  
- Personajes femeninos en narrativas visuales  
- Estética digital en redes sociales  
- Impacto emocional del lenguaje audiovisual  
- Colores, texturas y silencios como construcción de atmósferas  
""")

with tabs[4]:
    st.subheader("Participaciones Formativas")
    st.markdown("""
- Curso de Narrativa Audiovisual (PUCP)  
- Cursos clave en guion, lenguaje visual y fotografía  
Estas experiencias han sido fundamentales en mi formación como comunicadora audiovisual.
""")

with tabs[5]:
    st.subheader("Gustos e Inspiraciones")
    st.markdown("""
- Escuchar música: K-pop, Taylor Swift, playlists suaves  
- Ver k-dramas y series con una estética cuidada  
- Disfrutar de una taza de té como ritual creativo  
- Pasar tiempo con mi mascota Maya, que acompaña mis momentos de inspiración  
""")

with tabs[6]:
    st.subheader("Contacto")
    st.markdown("""
Si deseas comunicarte conmigo, puedes escribirme a:  
📬 **thaisgchoque@gmail.com**

st.markdown("### ¿Quieres que te escriba de vuelta?")
contacto_usuario = st.text_input("Déjame tu correo o red social preferida:")
if contacto_usuario:
    st.success("¡Gracias! Me pondré en contacto contigo pronto. ✉️")

Gracias por visitar este espacio 🌸
""")
