# import numpy as np

# def generate_packet_times(ue):
#     """
#     Génère les temps de début et de fin de transmission de paquets pour une UE donnée.
    
#     Args:
#     ue: Un objet UE contenant les paramètres de l'application en cours d'exécution.
    
#     Returns:
#     start_TX: Liste contenant les temps de début de transmission pour chaque paquet.
#     end_TX: Liste contenant les temps de fin de transmission pour chaque paquet.
#     """
#     # Initialisation des listes pour les temps de début et de fin de transmission
#     start_TX = []
#     end_TX = []

#     # Définition du temps actuel de départ à 0
#     current_time = 0

#     # Calcul de la durée de transmission d'un seul paquet basée sur le nombre de bits et la bande passante
#     # Pour ce faire, on assume une bande passante constante (par exemple, 100 Mbps pour la simplicité)
#     # Cette valeur devrait être ajustée selon la bande passante réelle disponible
#     bandwidth_mbps = 100
#     bits_per_millisecond = bandwidth_mbps * 1e3

#     # La boucle continue jusqu'à ce que le temps actuel dépasse le temps final de la simulation (e.g., 5000 ms)
#     while current_time < ue.tfinal:
#         # Générer le temps d'inter-arrivée du paquet suivant selon la loi spécifiée pour l'application de l'UE
#         if ue.delay_law == "exp":
#             inter_arrival_time = np.random.exponential(ue.delay_xpacket)
#         elif ue.delay_law == "uniform":
#             lower_bound = ue.delay_xpacket * (1 - ue.delay_percent)
#             upper_bound = ue.delay_xpacket * (1 + ue.delay_percent)
#             inter_arrival_time = np.random.uniform(lower_bound, upper_bound)
#         else:
#             raise ValueError("Loi de probabilité non supportée pour le temps d'inter-arrivée des paquets.")

#         # Ajouter le temps d'inter-arrivée au temps actuel pour obtenir le début de la transmission du paquet suivant
#         current_time += inter_arrival_time
#         start_TX.append(current_time)

#         # Générer la longueur du paquet suivant selon la loi spécifiée
#         if ue.R_law == "uniform":
#             packet_length = np.random.uniform(ue.R * (1 - ue.R_percent), ue.R * (1 + ue.R_percent))
#         else:
#             raise ValueError("Loi de probabilité non supportée pour la longueur des paquets.")

#         # Calculer le temps de transmission du paquet en divisant la longueur du paquet par le nombre de bits par milliseconde
#         # Cela donne la durée nécessaire pour transmettre le paquet à la bande passante spécifiée
#         transmission_time = packet_length / bits_per_millisecond

#         # Le temps de fin de transmission est le temps de début plus le temps de transmission
#         end_TX.append(current_time + transmission_time)

#     return start_TX, end_TX

# # Création d'un objet UE fictif pour le test
# class FakeUE:
#     def __init__(self):
#         self.tfinal = 5000  # Temps final de simulation
#         self.delay_law = "exp"  # Loi pour le temps d'inter-arrivée
#         self.delay_xpacket = 200  # Temps moyen d'inter-arrivée pour exp
#         self.R = 400000  # Longueur moyenne de paquet en bits
#         self.R_law = "uniform"  # Loi pour la longueur des paquets
#         self.R_percent = 0.2  # Variation de la longueur des paquets
#         self.delay_percent = 0.3  # Variation du temps d'inter-arrivée pour uniforme

# # Utilisation de l'exemple
# ue_example = FakeUE()
# start_times, end_times = generate_packet_times(ue_example)

# # Affichage des résultats (partiellement pour éviter une sortie trop longue)
# print("Débuts de transmission (extrait):", start_times[:5])
# print("Fins de transmission (extrait):", end_times[:5])
import sys
import math
import yaml
import random
import os
import argparse
import subprocess
import matplotlib.pyplot as plt
import numpy as np


fichier_de_cas = "ts_eq79_cas.yaml"

def get_from_dict(key, data, res=None, curr_level = 1, min_level = 1):
    """Fonction qui retourne la valeur de n'importe quel clé du dictionnaire
       key: clé associé à la valeur recherchée
       data: dictionnaire dans lequel il faut chercher
       les autres sont des paramètres par défaut qu'il ne faut pas toucher"""
    if res:
        return res
    if type(data) is not dict:
        msg = f"get_from_dict() works with dicts and is receiving a {type(data)}"
       # ERROR(msg, 1)
    else:
        # data IS a dictionary
        for k, v in data.items():
            if k == key and curr_level >= min_level:
                #print(f"return data[k] = {data[k]} k = {k}")
                return data[k]
            if type(v) is dict:
                level = curr_level + 1
                res = get_from_dict(key, v, res, level, min_level)
    return res 

def generate_transmission_times(app_config, tstart, tfinal):
    """
    Génère les listes des temps de début et de fin de transmission de paquets pour une application UE donnée.
    
    Args:
    - app_config : dict contenant la configuration de l'application du UE (incluant la loi de distribution du temps d'inter-arrivée, la longueur des paquets, etc.).
    - tstart : float, le temps de début de la simulation.
    - tfinal : float, le temps de fin de la simulation.
    
    Returns:
    - start_TX : Liste des temps de début de transmission de paquets.
    - end_TX : Liste des temps de fin de transmission de paquets.
    """
    
    current_time = tstart  # Initialiser le temps actuel à tstart
    start_TX = []  # Initialiser la liste des temps de début de transmission
    end_TX = []    # Initialiser la liste des temps de fin de transmission
    
    while current_time < tfinal:
        # Générer le temps d'inter-arrivée basé sur la loi de distribution spécifiée
        if app_config['delay_law'] == 'exp':  # Si la loi est exponentielle
            inter_arrival_time = np.random.exponential(app_config['delay_xpacket'])  # Générer le temps d'inter-arrivée selon une distribution exponentielle
        elif app_config['delay_law'] == 'uniform':  # Si la loi est uniforme
            min_delay = app_config['delay_xpacket'] * (1 - app_config['delay_percent'])  # Calculer la borne inférieure
            max_delay = app_config['delay_xpacket'] * (1 + app_config['delay_percent'])  # Calculer la borne supérieure
            inter_arrival_time = np.random.uniform(min_delay, max_delay)  # Générer le temps d'inter-arrivée selon une distribution uniforme
        
        # Calculer le temps de début de la prochaine transmission
        start_TX.append(current_time)
        
        # Calculer la longueur du paquet
        if app_config['R_law'] == 'uniform':  # Si la loi est uniforme
            min_length = app_config['R'] * (1 - app_config['R_percent'])  # Calculer la borne inférieure
            max_length = app_config['R'] * (1 + app_config['R_percent'])  # Calculer la borne supérieure
            packet_length = np.random.uniform(min_length, max_length)  # Générer la longueur du paquet selon une distribution uniforme
        
        # Estimer le temps de transmission basé sur la longueur du paquet et la vitesse de transmission (simplifié ici)
        # Cette partie dépend de la vitesse de transmission, qui n'est pas spécifiée, donc nous utilisons une approximation
        transmission_time = packet_length / 1e6 # Supposons une vitesse de 1 Mbps pour l'exemple
        
        # Calculer le temps de fin de la transmission
        end_TX.append(current_time + transmission_time)
        
        # Mettre à jour le temps actuel
        current_time += inter_arrival_time
    
    return start_TX, end_TX

# Fonction pour lire le fichier YAML et extraire tstart et tfinal
def get_tstart_tfinal_from_yaml(yaml_file_path):
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
        tstart = get_from_dict('tstart', data)
        tfinal = get_from_dict('tfinal', data)
    return tstart, tfinal

# Exemple d'utilisation
yaml_file_path = 'ts_eq79_cas.yaml'
tstart, tfinal = get_tstart_tfinal_from_yaml(yaml_file_path)

# Configuration de l'application Streaming 4K
app_config_streaming_4k = {
    'delay_xpacket': 200,
    'delay_law': 'exp',
    'R': 400000,
    'R_law': 'uniform',
    'R_percent': 0.2,
}

# Générer les temps de début et de fin de transmission
start_TX, end_TX = generate_transmission_times(app_config_streaming_4k, tstart, tfinal)

# Afficher les premiers éléments pour vérifier
print("Débuts de transmission (premiers éléments):", start_TX[:5])
print("Fins de transmission (premiers éléments):", end_TX[:5])







def generate_packet_lengths(app_config, num_transmissions):
    """
    Génère la liste des longueurs de paquets envoyés à chaque transmission de l'application de l'UE.
    
    Args:
    - app_config : dict contenant la configuration de l'application du UE (incluant la loi de distribution de la longueur des paquets, etc.).
    - num_transmissions : int, nombre total de transmissions à générer.
    
    Returns:
    - packet_lengths : Liste des longueurs de paquets envoyés à chaque transmission.
    """
    packet_lengths = []  # Initialiser la liste des longueurs de paquets
    #?? peux-etre mettre une condition sur le num_transmission en fonction de RB dispo??
    for _ in range(num_transmissions):
        # Calculer la longueur du paquet
        if app_config['R_law'] == 'uniform':  # Si la loi est uniforme
            min_length = app_config['R'] * (1 - app_config['R_percent'])  # Calculer la borne inférieure
            max_length = app_config['R'] * (1 + app_config['R_percent'])  # Calculer la borne supérieure
            packet_length = np.random.uniform(min_length, max_length)  # Générer la longueur du paquet selon une distribution uniforme
        packet_lengths.append(packet_length)  # Ajouter la longueur du paquet à la liste
    
    return packet_lengths

# Exemple d'utilisation
app_config_streaming_4k = {
    'R': 400000,
    'R_law': 'uniform',
    'R_percent': 0.2,
}

num_transmissions = 10  # Nombre total de transmissions à générer

# Générer les longueurs de paquets envoyés à chaque transmission de l'application de l'UE
packet_lengths = generate_packet_lengths(app_config_streaming_4k, num_transmissions)

# Afficher la liste des longueurs de paquets
print("Longueurs de paquets envoyés à chaque transmission:", packet_lengths)
