import { useState } from 'react'

function App() {
  const [funcion, setFuncion] = useState('')
  const [resultado, setResultado] = useState('')

  const calcular = async () => {
    const response = await fetch(`http://localhost:8000/integral?funcion=${funcion}`)
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
      <button onClick={calcular}>Calcular</button>
      <p>Resultado: {resultado}</p>
    </div>
  )
}

export default App