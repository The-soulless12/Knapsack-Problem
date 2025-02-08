objets = [
        {'emoji': '💎', 'nom': 'Diamant', 'valeur': 100, 'poids': 2},
        {'emoji': '📱', 'nom': 'Smartphone', 'valeur': 80, 'poids': 1},
        {'emoji': '⌚', 'nom': 'Montre', 'valeur': 50, 'poids': 1},
        {'emoji': '🎸', 'nom': 'Guitare', 'valeur': 60, 'poids': 3},
        {'emoji': '🎮', 'nom': 'Console', 'valeur': 90, 'poids': 2},
        {'emoji': '💻', 'nom': 'Ordinateur', 'valeur': 120, 'poids': 4},
        {'emoji': '📷', 'nom': 'Caméra', 'valeur': 70, 'poids': 2},
        {'emoji': '🏀', 'nom': 'Ballon', 'valeur': 30, 'poids': 1},
        {'emoji': '🎧', 'nom': 'Casque', 'valeur': 40, 'poids': 1},
        {'emoji': '📚', 'nom': 'Livre', 'valeur': 20, 'poids': 2},
        {'emoji': '👜', 'nom': 'Sac de luxe', 'valeur': 110, 'poids': 3},
        {'emoji': '🥪', 'nom': 'Sandwich', 'valeur': 50, 'poids': 1},
        {'emoji': '🏡', 'nom': 'Maquette maison', 'valeur': 200, 'poids': 5},
        {'emoji': '🎻', 'nom': 'Violon', 'valeur': 95, 'poids': 3},
        {'emoji': '🥾', 'nom': 'Chaussures', 'valeur': 55, 'poids': 2},
    ]

def afficherObjets():
    print("\n📦 Liste des objets disponibles :\n")
    print(f"{'  ':<1} | {'Nom':<15} | {'Valeur':<7} | {'Poids':<5}")
    print("-" * 40)
    for obj in objets:
        print(f"{obj['emoji']:<1} | {obj['nom']:<15} | {obj['valeur']:<7} | {obj['poids']:<5}")

def Knapsack(capacite):
    print(f"\n🔍 Résolution du problème pour une capacité de {capacite} kg...")
    # Implémentation du solveur à ajouter ici
    return 0

def main():
    while True:
        print("\nMenu:")
        print("1. Afficher les objets")
        print("2. Trouver la solution")
        print("3. Quitter")
        choix = input("Entrez votre choix: ")
        
        if choix == "1":
            afficherObjets()
        elif choix == "2":
            capacite = int(input("Entrez la capacité du sac à dos: "))
            Knapsack(capacite)
        elif choix == "3":
            print("👋 Programme terminé.")
            break
        else:
            print("⚠️ Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()