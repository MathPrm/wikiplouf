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
        <div className="animal-card-category">
          <span className="category-label">Groupe :</span>
          <span className="category-name">
            {animal.category_name || "Non classé"}
          </span>
        </div>
        {animal.tag_names && animal.tag_names.length > 0 && (
          <div className="animal-card-tags">
            {animal.tag_names.map((tag, index) => (
              <span key={index} className="tag-badge">#{tag}</span>
            ))}
          </div>
        )}
        <button className="animal-card-button">
          Voir le détail
        </button>
      </div>
    </div>
  );
};

export default AnimalCard;