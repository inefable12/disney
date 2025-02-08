import streamlit as st
import random
import time

def main():
    st.title("🎬 Adivina la Película con Emojis! 🍿")
    st.write("Adivina el nombre de la película de Disney basándote en los emojis. ¡Buena suerte!")

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
    puntaje = 0

    for emoji, pelicula_correcta in peliculas.items():
        st.subheader(f"¿Qué película es? {emoji}")
        opciones_mezcladas = random.sample(opciones, 4)
        if pelicula_correcta not in opciones_mezcladas:
            opciones_mezcladas[random.randint(0, 3)] = pelicula_correcta
        
        respuesta = st.radio("Selecciona una opción:", opciones_mezcladas, key=emoji)
        
        if respuesta == pelicula_correcta:
            puntaje += 1
    
    if st.button("Ver resultado"):
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
