import streamlit as st
import random

# Configuración
st.set_page_config(layout="wide", page_title="Portafolio de Thais Choque")

# Estilos visuales
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #fdf1f1;
    color: #2e2e2e;
    font-family: 'Georgia', serif;
}
.container {
    display: flex;
    min-height: 100vh;
}
.sidebar {
    background-color: #f8e6e9;
    width: 300px;
    padding: 2rem 1rem;
    text-align: center;
}
.sidebar img {
    border-radius: 50%;
    width: 160px;
}
.content {
    flex-grow: 1;
    padding: 2rem 3rem;
}
.stTabs [role="tablist"] {
    justify-content: center;
}
h1, h2, h3 {
    color: #772f40;
}
.stButton button {
    background-color: #772f40;
    color: white;
    border-radius: 5px;
}
</style>

<div class="container">
  <div class="sidebar">
    <img src="mi_foto_circular.png" alt="Thais Choque">
    <h2 style="color:#772f40;">Thais Choque</h2>
    <p>Estudiante de Comunicación Audiovisual<br>PUCP 🎬</p>
    <hr>
    <em style="color:#555;">""" + random.choice([
    "“Lo más importante no es la cámara, sino el ojo.” – Alfred Eisenstaedt",
    "“Cada plano es una emoción esperando ser descubierta.”",
    "“El cine también es una forma de escuchar.”",
    "“La sensibilidad guía la mirada.”"
]) + """</em>
    <hr>
    <p><strong>📫 Contacto:</strong><br>thaisgchoque@gmail.com</p>
    <br>
    <form>
      <input type="text" name="correo" placeholder="Tu contacto preferido" style="padding:8px;width:90%;border-radius:5px;border:1px solid #ccc;">
    </form>
  </div>
  <div class="content">
""", unsafe_allow_html=True)

# Tabs en el panel derecho
tabs = st.tabs(["Inicio", "Resume", "Exploraciones Creativas", "Research", "Hobbies", "Contacto"])

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

¿Hay algo que quieras decirme?
""")
    mensaje = st.text_area("💌 Tu mensaje")
    if mensaje:
        st.success("¡Gracias por compartir tus palabras conmigo!")

# Cierre de la estructura visual
st.markdown("</div></div>", unsafe_allow_html=True)
