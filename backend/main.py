from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from matplotlib import pyplot as plt
import numpy as np
import sympy as sp
import io
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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
            "resultado" : str(resultado),
            "latex": sp.latex(resultado)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/derivada")
def calcular_derivada(funcion: str):
    try: 
        f = sp.sympify(funcion)
        resultado = sp.diff(f, x)
        return {
            "resultado" : str(resultado),
            "latex": sp.latex(resultado)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/resolver-ecuacion")
def resolver_ecuacion(funcion: str):
    try:
        f = sp.sympify(funcion)
        resultado = sp.solve(f, x)
        return {
            "resultado" : str(resultado),
            "latex": sp.latex(resultado)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/grafico")
def grafico(funcion: str):
    try:
        f=sp.sympify(funcion)
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

        buf = io.BytesIO()           # 创建一个内存缓冲区
        plt.savefig(buf, format='png')  # 把图像保存进去
        buf.seek(0)                  # 回到开头
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return {"imagen": img_base64}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))