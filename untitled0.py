import streamlit as st
import random

# Configuración
st.set_page_config(layout="wide", page_title="Portafolio de Thais Choque")

# Estilos personalizados
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #fdf1f1;
        color: #2e2e2e;
        font-family: 'Georgia', serif;
    }
    .stApp {
        background-color: #fdf1f1;
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
    </style>
""", unsafe_allow_html=True)

# Frase inspiradora aleatoria
frases = [
    "“Lo más importante no es la cámara, sino el ojo.” – Alfred Eisenstaedt",
    "“Cada plano es una emoción esperando ser descubierta.”",
    "“El cine también es una forma de escuchar.”",
    "“La sensibilidad guía la mirada.”"
]
frase_aleatoria = random.choice(frases)

# Layout principal: lateral izquierda y contenido derecha
col1, col2 = st.columns([1, 3])

# -----------------------
# 📌 Columna izquierda
with col1:
    st.image("mi_foto_circular.png", width=200)
    st.markdown("<h2 style='color:#772f40;'>Thais Choque</h2>", unsafe_allow_html=True)
    st.markdown("Estudiante de Comunicación Audiovisual en la PUCP 🎬")
    st.markdown("---")
    st.markdown(f"<em style='color:#555;'>{frase_aleatoria}</em>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("📫 **Contacto:** thaisgchoque@gmail.com")
    contacto_usuario = st.text_input("¿Te gustaría que te escriba de vuelta?")
    if contacto_usuario:
        st.success("¡Gracias! Me pondré en contacto contigo pronto. ✨")

# -----------------------
# 📁 Columna derecha: Tabs
with col2:
    tabs = st.tabs([
        "Inicio", "Resume", "Exploraciones Creativas", "Research", "Hobbies", "Contacto"
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
He trabajado con luz natural, retratos y composición. Me interesa cómo una imagen puede transmitir atmósferas sutiles.

**Análisis visual**  
Observar planos, ritmo narrativo y silencios significativos ha sido clave para enriquecer mi comprensión del lenguaje cinematográfico.

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
- Colores, texturas y silencios como construcción de atmósferas
""")

    with tabs[4]:
        st.subheader("Gustos e Inspiraciones")
        st.markdown("""
- Escuchar música: K-pop, Taylor Swift, playlists suaves  
- Ver k-dramas y series con una estética cuidada  
- Disfrutar de una taza de té como ritual creativo  
- Pasar tiempo con mi mascota Maya, que acompaña mis momentos de inspiración  
""")

    with tabs[5]:
        st.subheader("Contacto")
        st.markdown("""
Puedes escribirme a:  
📬 **thaisgchoque@gmail.com**

Gracias por visitar este espacio 🎀
""")
