#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

prelude="Je suis désolé, maitre..."
first_fixed="c'est parce que "
first_var=["un zombie","le troll érudit","l'un des gardiens","un rat mutant","l'aubergiste","le bourreau ivre","un ménestrel moche","le gobelin de ménage","un orque d'élite","le sorcier stagiare","un type suspect","le prisonnier barbu","l'herboriste","le chien d'un voisin","un garde de la ville","un colporteur","un aventurier","le plombier","l'ingénieur gobelin","un vieux fou"]
second_var=["a glissé","a dérapé","a cassé un bidule","a brisé un truc","a vomi","a perdu ses clées","a fait ses besoins","était bloqué","s'est perdu","est tombé","s'est emdormi","a passé la nuit","s'est reveillé","s'est tué","s'est fait mal","a trébuché","était coincé","s'est battu","a cause des ennuis","a mis le feu"]
second_fixed=" dans "
third_var=["la cave","le souterrain nord","le grenier","mon bureau","la remise a ingredient","les cuisines","la niche des chiens","la volière a corbeaux","la fosse a scorpions","votre bureau","l'escalier du deuxieme niveau","le bac du limon glaireux","le couloir principal","le hangar de bricolage","l'atelier de forge","la salle de fouettage","le dortoir des orques","l'antre du Golbargh","le magasin","votre bibliothèque"]
third_fixed="\n ... et tout ça... a cause "
fourth_var=["de cette bète","de cette stupide","d'une grosse","d'une infame","d'une étrange","d'une incroyable","de l'improbable","de la fameuse","de cette imbécile de","de la ridicule",", c'est ballot, de la","de l'existance d'une","de l'embuche causée par une","du piège que représentait une","de la présence de cette","vous allez rire, d'une","c'est bien dommage, de la","de la position d'une","de son penchant pour une","d'une médiocre"]
fifth_var=["brouette rouillée","manivelle tordue","scie abimée","bassine oubliée","cle de douze","corbeille de linge","hallebarde tordue","chouette empaillée","terrine piegée","flute empoisonnée","tête de goule","faux venimeuse","guitare disloquée","bielle biscornue","salière brisée","peau de banane","perruque décrépite","chaussette rouge","babouche verte","pantoufle usée"]
fouth_fixed=" qui "
sixth_var=["venait de ma grand-mère","était justement la","est apparue comme par magie","venait de votre cousin","avait ete abandonnée","était suspecte","n'aurait pas du se trouver la","avait justement l'air fourbe","était dans l'ombre","n'avait l'air de rien","a été laissée par un voisin","était bel et bien dangereuse","était pourtant chère","avait une odeur inquiétante","avait changé de place","aurait du être rangée","vous appartient","s'est revélée glissante","était peut-etre a moi","pose toujours des problèmes"]
finish="... donc c'est pas ma faute !"

string=prelude
string+="\n"
string+=first_fixed
string+=first_var[random.randint(0,len(first_var)-1)]
string+=" "
string+=second_var[random.randint(0,len(second_var)-1)]
string+=second_fixed
string+=third_var[random.randint(0,len(third_var)-1)]
string+=third_fixed
string+=fourth_var[random.randint(0,len(fourth_var)-1)]
string+=" "
string+=fifth_var[random.randint(0,len(fifth_var)-1)]
string+=fouth_fixed
string+=sixth_var[random.randint(0,len(sixth_var)-1)]
string+="\n"
string+=finish

print string


