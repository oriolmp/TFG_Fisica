import os

for sociodem_entry in ["genere", "edat", "pp", "p_cuid", "p_g1", "p_g2", "p_l", "p_ac"]:
    for layer_tp in ["uniplex", "multiplex"]:
        os.system("python3 play_with_data_fran_networks_apart.py "+sociodem_entry+" "+layer_tp)

for story in ["Compartir", "Ingresada", "Experiencia_aprenentatge",#'capacitation_Teatre_Amigues', 'Obrir_camí', 'Experiencia_aprenentatge', 'Gossos', 'Sanglotant'
             ]:
    for layer_tp in ["uniplex", "multiplex"]:
        os.system("python3 play_with_data_fran_networks_no_cats.py "+story+" "+layer_tp)
