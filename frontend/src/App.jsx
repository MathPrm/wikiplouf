import React from 'react';
import './App.css';
import AnimalListContainers from './containers/AnimalListContainers/AnimalListContainers';

function App() {
  return (
    <div className="App">
      <header style={headerStyle}>
        <h1>WikiPlouf</h1>
        <p>Explorez les profondeurs de l'océan</p>
      </header>
      
      <main>
        <AnimalListContainers />
      </main>
      
      <footer style={footerStyle}>
        <p>© 2026 WikiPlouf - Projet Étudiant</p>
      </footer>
    </div>
  );
}

const headerStyle = {
  backgroundColor: '#1a1a1a',
  padding: '20px',
  marginBottom: '20px',
  borderBottom: '2px solid #646cff'
};

const footerStyle = {
  marginTop: '40px',
  padding: '20px',
  color: '#888',
  fontSize: '0.9em'
};

export default App;