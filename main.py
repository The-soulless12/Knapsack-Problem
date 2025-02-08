objets = [
        {'emoji': '💎', 'nom': 'Diamant', 'valeur': 100, 'poids': 3},
        {'emoji': '📱', 'nom': 'Smartphone', 'valeur': 80, 'poids': 1},
        {'emoji': '⌚', 'nom': 'Montre', 'valeur': 50, 'poids': 1},
        {'emoji': '🎸', 'nom': 'Guitare', 'valeur': 30, 'poids': 3},
        {'emoji': '🎮', 'nom': 'Console', 'valeur': 90, 'poids': 2},
        {'emoji': '💻', 'nom': 'Ordinateur', 'valeur': 120, 'poids': 4},
        {'emoji': '📷', 'nom': 'Caméra', 'valeur': 70, 'poids': 2},
        {'emoji': '🏀', 'nom': 'Ballon', 'valeur': 50, 'poids': 1},
        {'emoji': '🎧', 'nom': 'Casque', 'valeur': 10, 'poids': 1},
        {'emoji': '📚', 'nom': 'Livres', 'valeur': 20, 'poids': 2},
        {'emoji': '👜', 'nom': 'Sac de luxe', 'valeur': 110, 'poids': 4},
        {'emoji': '🥪', 'nom': 'Sandwich', 'valeur': 50, 'poids': 1},
        {'emoji': '🏡', 'nom': 'Maquette maison', 'valeur': 200, 'poids': 5},
        {'emoji': '🎻', 'nom': 'Violon', 'valeur': 95, 'poids': 3},
        {'emoji': '🥾', 'nom': 'Chaussures', 'valeur': 55, 'poids': 2},
    ]

def afficherObjets():
    print("\n📦 Liste des objets disponibles :")
    print(f"{'  ':<1} | {'Nom':<15} | {'Valeur':<7} | {'Poids':<5}")
    print("-" * 40)
    for obj in objets:
        print(f"{obj['emoji']:<1} | {obj['nom']:<15} | {obj['valeur']:<7} | {obj['poids']:<5}")

def Knapsack(capacite):
    # Cette fonction résout le problème du Knapsack en utilisant la programmation dynamique
    print(f"\n🔍 Résolution du problème pour une capacité de {capacite} ...")
    n = len(objets)
    
    # dp[w] stocke la valeur maximale pouvant être obtenue avec une capacité w
    # Le tableau dp évite de recalculer plusieurs fois la même combinaison
    dp = [0] * (capacite + 1)
    choix = [[False] * (capacite + 1) for _ in range(n)] # Ce tableau permet de suivre les objets sélectionnés
    
    for i, obj in enumerate(objets):
        poids, valeur = obj['poids'], obj['valeur']
        
        for w in range(capacite, poids - 1, -1):  # On parcours en inverse pour éviter d’écraser les valeurs précédentes
            if dp[w] < dp[w - poids] + valeur: # Si ajouter cet objet améliore la valeur maximale pour w
                dp[w] = dp[w - poids] + valeur  # On met à jour la meilleure valeur obtenue
                choix[i][w] = True  # On marque cet objet comme pris pour ce poids
    print(f"\n💼 Valeur maximale obtenue : {dp[capacite]} et les objets sélectionnés sont :")

    w = capacite
    for i in range(n - 1, -1, -1):
        if choix[i][w]:  
            print(f"{objets[i]['emoji']} {objets[i]['nom']} (Valeur: {objets[i]['valeur']}, Poids: {objets[i]['poids']})")
            w -= objets[i]['poids']

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