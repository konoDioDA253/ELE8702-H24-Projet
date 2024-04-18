# Cette classe est utilise pour repertorier les caracteristiques d'une antenne 
class Antenna:

     def __init__(self, id):
        self.id = id          #id de l'antenne (int)
        self.frequency = None # Antenna frequency in GHz
        self.height = None    # Antenna height
        self.group = None     # group défini dans la base de données (str)
        self.coords = None    # tuple contenant les coordonnées (x,y) 
        self.assoc_ues = []   # liste avec les id des UEs associés à l'antenne
        self.scenario = None  # pathloss scénario tel que lu du fichier de cas (str)
        self.gen = None       # type de géneration de coordonnées: 'g', 'a', etc. (str)
        # Attributs rajoutes par notre equipe
        self.type = None      # Type de l'antenne
        self.name = None      # Nom de l'Antenne
        self.gain = None      # Gain de l'antenne
        self.nbits = []       # Liste des Nombres de bits recus a chaque slot de temps dt
        self.live_ues = []    # Regroupement des ID des ues qui auront transmis a chaque dt
        self.nombre_resource_blocks_max = None      # Nombre de resource blocks maximal theorique (calculer avec SCS et BW)
        self.nombre_resource_blocks_disponibles = [] # !! Liste du Nombre de resource blocks disponibles a chaque slot de temps dt
        self.FR_type = None   # Spécifie si l'UE aura une communication FR1 ou FR2 avec son antenne associee
        self.bandwidth = None # Spécifie la largeur de bande de l'antenne
        self.sub_carrier_spacing = None       # Espacement entre sous-porteuse que l'antenne supporte


# Cette classe est utilise pour repertorier les caracteristiques d'une UE 
class UE:

     def __init__(self, id, app_name):
        self.id= id           # id de l'UE (int)
        self.height = None    # UE height
        self.group = None     # group défini dans la base de données (str)
        self.coords=None      # tuple contenant les coordonnées (x,y) 
        self.app=app_name     # nom de l'application qui tourne dans le UE (str)
        self.assoc_ant=None   # id de l'antenne associée à l'UE (int)
        self.los = True       # LoS ou non (bool)
        self.gen = None       # type de géneration de coordonnées: 'g', 'a', etc. (str)
        # Attributs rajoutes par notre equipe
        self.type = None      # Type de l'UE
        self.name = None      # Nom de l'UE
        self.nbits = []       # Nombre de bits envoyes a chaque slot de temps dt
        self.start_TX = []    # !! Liste des temps de debuts de transmission de paquets
        self.end_TX = []      # !! Liste des temps de fins de transmission de paquets
        self.cqi = None       # CQI de l'UE avec son antenne
        self.Fncy = None # Efficacité de la transmission avec l'antenne (obtenue a partir du CQI)
        self.TX_bits = []   # !! Liste des longueurs de paquet envoyés à chaque transmission de l'application de l'UE
        self.TX_law = None   # Loi de probabilite suivi par la longueur de paquets de l'application de l'UE
        self.TX_percent = None   # Precision de la longueur du paquet de l'application de l'UE (seulement dans le cas d'une loi uniforme)
        self.delay_xpacket = []   # !! Liste des temps d'envoi inter-paquet de l'application de l'UE (Liste specifiant le temps écoulé entre le début de l'envoi de deux paquets, c'est un cutoff time)
        self.delay_law = None   # Loi de probabilite suivie par le temps d'arrivee inter-paquet de l'application de l'UE
        self.delay_percent = None   # Precision du temps d'arrivee inter-paquet de l'application de l'UE (seulement dans le cas d'une loi uniforme)
        self.buffer = []        # Liste contenant la quantité de bits non envoyés par manque de Resource Block disponibles du coté de l'antenne associée a chaque slot de temps dt 
        self.resource_blocks_alloues = [] # Quantite de resources blocks alloues a chaque slot de temps dt


antennas = []
ues = []
antenna = Antenna(0)
antenna.group = "Antenna1"
antenna.coords = [83.0, 551.0]
ue1 = UE(0,"app1")
ue1.group = "UE1-App1"
ue1.start_TX = [ 0.02412, 0.37425, 0.531779, 0.604295, 0.832996]
ue1.end_TX = [ 0.02642, 0.39425, 0.551779, 0.644295, 0.852996]
ue1.coords = [2500, 1142.8571]
ue2 = UE(0,"app1")
ue2.group = "UE1-App1"
ue2.start_TX = [ 0.1349, 0.50440, 0.7929199, 0.83611]
ue2.end_TX = [ 0.1369, 0.56440, 0.8129199, 0.83911]
ue2.coords = [2500, 1142.8571]
ue3 = UE(0,"app1")
ue3.group = "UE1-App1"
ue3.start_TX = [ 0.1103, 0.6477, 0.6939, 0.7892, 0.8017]
ue3.end_TX = [ 0.1153, 0.6497, 0.6969, 0.7992, 0.8117]
ue3.coords = [2500, 1142.8571]
antenna.live_ues = [[], [25], [8, 25], [1, 8, 15], [1, 8, 15], [15, 23], [23], [23], [1, 15], [1, 8, 15]]
antenna.nbits = [0, 529, 1558, 3263, 3109, 1995, 1025, 1284, 225, 2441]
antennas.append(antenna)
ues.append(ue1)
ues.append(ue2)
ues.append(ue3)
temps_courant = 0.025
pas_temps = 0.001

def get_sorted_ues_for_time_slot(ues, temps_courant, pas_temps):
    sorted_ues = sorted(ues, key=lambda ue: next((tx_time for tx_time in ue.start_TX if tx_time > temps_courant), float('inf')))
    time_slot_end = temps_courant + pas_temps
    ues_sorted_for_time_slot = []
    for ue in sorted_ues:
        if any(tx_time < time_slot_end for tx_time in ue.end_TX):
            ues_sorted_for_time_slot.append(ue)
    return ues_sorted_for_time_slot

# Utilisation de la fonction
ues_sorted = get_sorted_ues_for_time_slot(ues, temps_courant, pas_temps)

print(ues_sorted[0].start_TX)
# print(ues_sorted[1].start_TX)
# print(ues_sorted[2].start_TX)