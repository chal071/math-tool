import { useState } from 'react'
import katex from 'katex'
import 'katex/dist/katex.min.css'

function App() {
  const [latex, setLatex] = useState('')
  const [imagen, setImagen] = useState('')
  const [funcion, setFuncion] = useState('') 

  const calcular = async (tipo) => {
    const response = await fetch(`http://localhost:8000/${tipo}?funcion=${encodeURIComponent(funcion)}`)
    const base64 = await fetch(`http://localhost:8000/grafico?funcion=${encodeURIComponent(funcion)}`)
    const data = await response.json()
    const graficoData = await base64.json()
    console.log(data.latex)   
    setImagen(graficoData.imagen)
    setLatex(data.latex.replace(/\\\\/g, '\\'))
  }

  const renderLatex = (tex) => {
    return { __html: katex.renderToString(tex, { throwOnError: false }) }
  }
  
  return (
    <div>
      <div className="header">
        <header>
          <h1>Herramienta de Matemáticas</h1>
        </header>
      </div>
      <div className="funcion">
        <p>
          Funcion:
        </p>
        <input 
            className="inputbox"
            value={funcion}
            onChange={(e) => setFuncion(e.target.value)}
            placeholder="Introduce una función"
          />
      </div>
      <div className="botones">
        <button onClick={() => calcular('integral')} className="boton">Calcular Integral</button>
        <button onClick={() => calcular('derivada') } className="boton">Calcular Derivada</button>
        <button onClick={() => calcular('resolver-ecuacion')} className="boton">Resolver Ecuacion</button>
      </div>
      {latex && <div dangerouslySetInnerHTML={renderLatex(latex)} />}
      <img src={`data:image/png;base64,${imagen}`} />
    </div>
  )
}

export default App