import streamlit as st
import random

def main():
    st.set_page_config(page_title="Adivina la Película", page_icon="🎬")
    st.title("🎬 Adivina la Película con Emojis! 🍿")
    st.write("Intenta adivinar el nombre de la película de Disney basándote en los emojis. ¡Buena suerte!")

    peliculas = {
        "🦁👑": "El Rey León",
        "🤖🌱": "WALL-E",
        "🧞‍♂️🕌": "Aladdín",
        "🐭🧀": "Ratatouille",
        "🚀👨‍🚀": "Toy Story",
        "🧊🐧": "Frozen",
        "🦆👴🎈": "Up",
        "🐠🔎": "Buscando a Nemo",
        "👸🐸": "La Princesa y el Sapo",
        "🐉👦": "Mulan"
    }

    opciones = list(peliculas.values())
    respuestas_usuario = {}

    with st.form("quiz_form"):
        for emoji, pelicula_correcta in peliculas.items():
            st.subheader(f"¿Qué película es? {emoji}")
            opciones_mezcladas = random.sample(opciones, 4)
            if pelicula_correcta not in opciones_mezcladas:
                opciones_mezcladas[random.randint(0, 3)] = pelicula_correcta
            
            respuestas_usuario[emoji] = st.radio("Selecciona una opción:", opciones_mezcladas, key=emoji)
        
        submit_button = st.form_submit_button("Ver resultado")
    
    if submit_button:
        puntaje = sum(1 for emoji, pelicula_correcta in peliculas.items() if respuestas_usuario[emoji] == pelicula_correcta)
        st.success(f"Tu puntaje: {puntaje}/10")
        
        if puntaje == 10:
            st.balloons()
            st.write("🎉 ¡Perfecto! ¡Eres un experto en películas de Disney! 🎈")
        elif puntaje >= 7:
            st.write("¡Muy bien! Sabes bastante de Disney! ✨")
        else:
            st.write("¡Sigue practicando! 🎥")

if __name__ == "__main__":
    main()
