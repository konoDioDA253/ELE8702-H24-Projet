# ELE8702-H24-Projet
Project of ELE8702 class 

## Quick Start Instructions

To quickly get started with the project, follow these steps:

1. **On your computer (Linux or Windows)**
   Open a terminal and execute the following commands:
```
git clone https://github.com/konoDioDA253/ELE8702-H24-Projet.git
cd ELE8702-H24-Projet/
```
2. **Equipment Coordinates Description**: 
   Describe the coordinates of your equipments in the `ts_eq79_coords.txt` file. This file should contain the coordinates of your geometry in the EXACT following format : 
```
antenna	ID	Type	COORDX	COORDY
UE	ID	TYPE	COORDX	COORDY	APPNAME
```
Here is an example with UEs from an app called "Controle-Drone" :
```
antenna	0	Antenna3	1666.6666666666667	800.0
antenna	1	Antenna3	3333.3333333333335	800.0
antenna	2	Antenna3	1666.6666666666667	1600.0
antenna	3	Antenna3	3333.3333333333335	1600.0
antenna	4	Antenna3	1666.6666666666667	2400.0
antenna	5	Antenna3	3333.3333333333335	2400.0
antenna	6	Antenna3	2500.0	3200.0
ue	0	UE2-App2	674.5032755825313	773.5147031993723	Controle-Drone
ue	1	UE2-App2	1282.555374135416	1408.838074268255	Controle-Drone
ue	2	UE2-App2	1360.3773317814312	1737.6400658670022	Controle-Drone
ue	3	UE2-App2	2102.366226358535	435.374717091925	Controle-Drone
ue	4	UE2-App2	313.98126536675585	1420.8907262645885	Controle-Drone
ue	5	UE2-App2	444.85573543194386	1733.3680551947675	Controle-Drone
ue	6	UE2-App2	43.79751264957367	2143.668273407651	Controle-Drone
ue	7	UE2-App2	368.34647958254726	2777.129452882241	Controle-Drone
ue	8	UE2-App2	2021.6321281541525	3941.407351378421	Controle-Drone
ue	9	UE2-App2	1313.4375585755306	1890.5704508877664	Controle-Drone
ue	10	UE2-App2	3754.3238912551064	1339.9873315533416	Controle-Drone
ue	11	UE2-App2	1742.4867363045921	2556.872620975223	Controle-Drone
ue	12	UE2-App2	4848.460700252123	3535.636672353437	Controle-Drone
ue	13	UE2-App2	2095.770059117438	2871.1539115012906	Controle-Drone
ue	14	UE2-App2	3395.5807062817876	1489.0663675619257	Controle-Drone
ue	15	UE2-App2	1175.5822240548273	314.4275360867599	Controle-Drone
ue	16	UE2-App2	4394.665775485212	229.57969442377725	Controle-Drone
ue	17	UE2-App2	2593.9619276572444	2150.6079736452466	Controle-Drone
ue	18	UE2-App2	731.5500290743771	2624.0709360914925	Controle-Drone
ue	19	UE2-App2	4579.200144675993	3104.7557463263242	Controle-Drone
ue	20	UE2-App2	1946.907073826137	506.7533653761987	Controle-Drone
ue	21	UE2-App2	4874.6729015207575	2068.896843128989	Controle-Drone
ue	22	UE2-App2	3148.4585085126887	3209.30430543863	Controle-Drone
ue	23	UE2-App2	1931.8445683008363	249.16100285724016	Controle-Drone
ue	24	UE2-App2	680.9429397526987	2674.1201009931324	Controle-Drone
ue	25	UE2-App2	1748.3488884133817	3484.437753841591	Controle-Drone
ue	26	UE2-App2	3701.082379594159	3921.776147614374	Controle-Drone
ue	27	UE2-App2	3344.5029374680857	1215.9193107679937	Controle-Drone
ue	28	UE2-App2	3955.754680379064	114.00387907885813	Controle-Drone
ue	29	UE2-App2	2608.43226778475	3485.707276931804	Controle-Drone
ue	30	UE2-App2	2574.080981890372	550.34862020567	Controle-Drone
ue	31	UE2-App2	2501.112430876365	2182.285506535905	Controle-Drone
ue	32	UE2-App2	1845.6337410010133	3573.8408072752586	Controle-Drone
ue	33	UE2-App2	1701.0641717403498	1087.7338021496967	Controle-Drone
ue	34	UE2-App2	2532.001132584759	813.8849330029798	Controle-Drone
ue	35	UE2-App2	1610.9640766790387	1593.2825535763477	Controle-Drone
ue	36	UE2-App2	4691.374180996688	322.36689010672296	Controle-Drone
ue	37	UE2-App2	986.2772496651851	798.7978787101983	Controle-Drone
ue	38	UE2-App2	4976.329803276344	3563.343997870564	Controle-Drone
ue	39	UE2-App2	971.622309930479	2258.933335807034	Controle-Drone
```

2. **Pathloss Computation Configuration**:
   Introduce changes in how the pathloss gets computed through the `ts_eq79_cas.yaml` file. Customize the parameters in this file to adjust the pathloss computation according to your requirements.

   Parameters of interest to modify here include the Geometry description, the start time and end time of the simulation (in miliseconds)

   In this file, you can also select the model and scenario used for pathloss calculation, the CQI table wanted, the processing speed of the UEs, the number of sub-carriers per Resource Block, the number of symbols per slot and the number of Resource Elements reserved for DMRS and other layers in the RB.

3. **Devices Database**:
   Specify your database of all possible devices (antennas and UEs description) with the `devices_db.yaml` file. This file should contain detailed descriptions of antennas and user equipment (UEs) that will be used in your simulations.

   Default parameters for the device database are given in the devices_db.yaml provided.

   Specify your database of all possible devices (antennas and UEs description) with the `devices_db.yaml` file. This file should contain detailed descriptions of antennas and user equipment (UEs) that will be used in your simulations.

   To determine the values for parameters such as bandwidth and subcarrier spacing (SCS), refer to the following reference tables:

   **For FR1 :**
   
   ![Tableau NRB FR1](tableau_NRB_FR1.png)

   **For FR2 :**

   ![Tableau NRB FR2](tableau_NRB_FR2.png)

4. **Antenna Support and Visibility**:
   - The program only supports one type of antenna at a time.
   - The visibility file (`visibility.txt`) specifies which antennas are in NLOS (Non-Line-of-Sight) situation with the UE. For example, `1 2 3` means UE 1 is in NLOS with Antennas 2 and 3. 
     - The visibility file needs to specify at least 5% and at most 30% of all UEs given in the `ts_eq79_coords.txt` file in NLOS.

5. **Running the Program**:
   To run the program, execute the following command in the terminal:
```
python ts_eq79.py ts_eq79_cas.yaml
```

6. **Graphical Output**:
After running the program, you will find a PDF containing all graphs in `ts_eq79_graphiques.pdf`.


## Dependencies

- **Package:** pdftk

### Installation Instructions:

#### Linux:
To install pdftk on Linux, please use your distribution's package manager:

- **Ubuntu/Debian:**

```
sudo apt install pdftk
```
- **Arch Linux:**
```
sudo pacman -S pdftk
```  

#### Windows:
Please install it by going to [this website](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) and downloading the .exe file. During installation, make sure to select the 'Add application directory to your environmental path' option.

## Plots :

![Disposition des equipements](disp_plot_disposition_equipements.png)

![Bits recus par slot](disp_average_traffic_per_slot.png)

![Traffic moyen des UEs](disp_average_traffic_ues.png)

![Traffic moyen des Antennas](disp_average_traffic_antennas.png)

![Proportion Paquets Envoyés par UE](disp_plot_packet_success_rate.png)

![Nombre de Resource Blocks alloués par UE](disp_plot_resource_blocks_per_ue.png)

## PDF of combined plots :

- [Lab 3 Graphiques](ts_eq79_graphiques.pdf)