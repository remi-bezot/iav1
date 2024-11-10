def calculate_reward(agent_performance):
    # Calcul de récompense basé sur la performance
    if agent_performance > 0.8:
        return 1.0  # Récompense maximale
    else:
        return 0.1  # Récompense faible
