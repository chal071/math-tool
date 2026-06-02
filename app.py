import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Herramienta de Matemáticas",
    page_icon="📐",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "funcion" not in st.session_state:
    st.session_state.funcion = ""

botones = {
    "√x": "sqrt(x)",
    "e^x": "exp(x)",
    "ln": "log(x)",
    "sin": "sin(x)",
    "cos": "cos(x)",
    "tan": "tan(x)",
    "log": "log(x, 10)",
    "arcsin": "asin(x)",
    "arccos": "acos(x)",
    "arctan": "atan(x)",
    "π": "pi",
    "⌫": "BORRAR",
    "C": "CLEAR"
}

x = sp.Symbol('x')

def plot_funcion(f, x):
    plt.figure()
    f_num = sp.lambdify(x, f, 'numpy')
    x_vals = np.linspace(-5, 5, 100)
    y = f_num(x_vals)
    y = np.full_like(x_vals, y) if np.isscalar(y) else y
    plt.plot(x_vals, y)
    plt.title("Grafico de la función")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)

    return plt.gcf()

def keyboard_input(f):
    filas = [
        ["1", "2", "3", "+", "-"],
        ["4", "5", "6", "*", "/"],
        ["7", "8", "9", "(", ")"],
        ["0", "x", "π", "**", "e^x"],
        ["sin", "cos", "tan", "ln", "log"],
        ["arcsin", "arccos", "arctan", "C", "⌫"],
    ]
    for fila in filas:
        cols = st.columns(len(fila))
        for i, col in enumerate(cols):
            with col:
                if st.button(fila[i]):
                    valor = botones.get(fila[i], fila[i])
                    if valor == "CLEAR":
                        st.session_state.funcion = ""
                    elif valor == "BORRAR":
                        st.session_state.funcion = st.session_state.funcion[:-1]
                    else:
                        st.session_state.funcion += valor
                    st.rerun()
    
    col1, col2 = st.columns(2)

    with col1:
        n = st.number_input("Raíz:", min_value=2, value=2, step=1)
        if st.button(f"ⁿ√x"):
            st.session_state.funcion += f"x**(1/{n})"
            st.rerun()

st.title("Herramienta de Matemáticas")

opcion = st.sidebar.selectbox(
    "Elige una herramienta:",
    ["Integral", "Derivada", "Resolver ecuación"]
)

st.header(f"Calculadora de {opcion}")


colLeft, colRight = st.columns(2)

with colLeft:
    funcion = st.text_input("Función:", 
                        value=st.session_state.funcion,
                        disabled=True)
    keyboard_funcion = keyboard_input(funcion)

with colRight:
    if opcion == "Integral":
        if funcion:
            try:
                f = sp.sympify(funcion)
                resultado = sp.integrate(f, x)

                st.write("**Función:**")
                st.latex(sp.latex(f))

                st.write("**Integral:**")
                st.latex(sp.latex(resultado))

            except Exception as e:
                st.error(f"Error: {e}")
    elif opcion == "Derivada":
        if funcion:
            try:
                f = sp.sympify(funcion)
                resultado = sp.diff(f, x)

                st.write("**Función:**")
                st.latex(sp.latex(f))

                st.write("**Derivada:**")
                st.latex(sp.latex(resultado))

            except Exception as e:
                st.error(f"Error: {e}")
    elif opcion == "Resolver ecuación":
        if funcion:
            try:
                f = sp.sympify(funcion)
                resultado = sp.solve(f, x)

                st.write("**Ecuación:**")
                st.latex(sp.latex(f) + " = 0")

                st.write("**Soluciones:**")
                st.latex(sp.latex(resultado))

            except Exception as e:
                st.error(f"Error: {e}")
    

    if funcion:
        try:
            f = sp.sympify(funcion)
            fig = plot_funcion(f, x)
            st.pyplot(fig)
        except:
            pass