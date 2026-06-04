import { useState } from 'react'

function App() {
  const [funcion, setFuncion] = useState('')
  const [resultado, setResultado] = useState('')

  const calcular = async (tipo) => {
    const response = await fetch(`http://localhost:8000/${tipo}?funcion=${encodeURIComponent(funcion)}`)
    const data = await response.json()
    setResultado(data.resultado)
  }
  
  return (
    <div>
      <h1>Herramienta de Matemáticas</h1>
      <input 
        value={funcion}
        onChange={(e) => setFuncion(e.target.value)}
        placeholder="Introduce una función"
      />
      <button onClick={() => calcular('integral')}>Calcular Integral</button>
      <button onClick={() => calcular('derivada')}>Calcular Derivada</button>
      <button onClick={() => calcular('resolver-ecuacion')}>Resolver Ecuacion</button>
      <p>Resultado: {resultado}</p>
    </div>
  )
}

export default App