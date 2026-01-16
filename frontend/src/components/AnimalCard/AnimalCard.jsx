import React from 'react';
import './AnimalCard.css';

const AnimalCard = ({ animal }) => {
  return (
    <div className="animal-card">
      {animal.thumb && (
        <img 
          src={animal.thumb} 
          alt={animal.name} 
          className="animal-card-image" 
        />
      )}
      <div className="animal-card-content">
        <h2 className="animal-card-title">{animal.name}</h2>
        <p className="animal-card-species">
          <strong>Espèce :</strong> {animal.species}
        </p>
        <p className="animal-card-description">
          {animal.description?.substring(0, 100)}...
        </p>
        <button className="animal-card-button">
          Voir le détail
        </button>
      </div>
    </div>
  );
};

export default AnimalCard;