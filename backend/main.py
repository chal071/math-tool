from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sympy as sp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_methods=["*"],
    allow_headers=["*"],
)

x = sp.Symbol('x')

@app.get("/integral")
def calcular_integral(funcion: str):
    try:
        f = sp.sympify(funcion)
        resultado = sp.integrate(f, x)
        return {
            "resultado" : str(resultado) 
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/derivada")
def calcular_derivada(funcion: str):
    try: 
        f = sp.sympify(funcion)
        resultado = sp.diff(f, x)
        return {
            "resultado" : str(resultado)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/resolver-ecuacion")
def resolver_ecuacion(funcion: str):
    try:
        f = sp.sympify(funcion)
        resultado = sp.solve(f, x)
        return {
            "resultado" : str(resultado)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))