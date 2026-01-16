import React, { useEffect, useState } from 'react';
import AnimalCard from '../../components/AnimalCard/AnimalCard';
import './AnimalListContainers.css'; // Importation du CSS dédié

// Composant "Smart" : gère uniquement la logique métier et l'accès aux données
const AnimalListContainer = () => {
  const [animals, setAnimals] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/animals/')
      .then(response => response.json())
      .then(data => {
        setAnimals(data);
        setLoading(false);
      })
      .catch(error => {
        console.error("Erreur API:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p className="loading-text">Chargement des animaux marins...</p>;

  return (
    <div className="animal-list-grid">
      {animals.map(animal => (
        <AnimalCard key={animal.id} animal={animal} />
      ))}
    </div>
  );
};

export default AnimalListContainer;