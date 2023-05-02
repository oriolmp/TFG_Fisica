import pickle
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import plotly.express as px
import matplotlib.font_manager as fm 
fm.findSystemFonts(fontpaths=None, fontext='otf')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Glacial Indifference'

figs = []

for sociodem_entry in ["genere", "edat", "pp", "p_cuid", "p_g1", "p_g2", "p_l", "p_ac"]:
    for layer_tp in ["uniplex", "multiplex"]:
        for story in ["pie", "Compartir", "Ingresada", "Experiencia_aprenentatge"]:
            figs.append(pickle.load(open('FigureObject_'+sociodem_entry+'_'+layer_tp+"_"+story+'.pickle', 'rb')))
            plt.savefig("../img/"+layer_tp+"_"+sociodem_entry+"_"+story+".pdf")
            plt.savefig("../img/"+layer_tp+"_"+sociodem_entry+"_"+story+".png")
      
for story in ["Compartir", "Ingresada", "Experiencia_aprenentatge"#'Obrir_camí', #'capacitation_Teatre_Amigues', 'Experiencia_aprenentatge',
       #'Gossos', 'Sanglotant'
       ]:
    for layer_tp in ["uniplex", "multiplex"]:
        figs.append(pickle.load(open('FigureObject_'+story+'_'+layer_tp+'.pickle', 'rb')))
        plt.savefig("../img/"+layer_tp+"_"+story+".pdf")
        plt.savefig("../img/"+layer_tp+"_"+story+".png")
#plt.show()
