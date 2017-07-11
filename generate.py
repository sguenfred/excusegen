# -*- coding: utf-8 -*-
import random

prelude="Je suis desole, maitre..."
first_fixed="c'est parce que "
first_var=["un zombie","le troll erudit","l'un des gardiens","un rat mutant","l'aubergiste","le bourreau ivre","un menestrel moche","le gobelin de menage","un orque d'elite","le sorcier stagiare","un type suspect","le prisonnier barbu","l'herboriste","le chien d'un voisin","un garde de la ville","un colporteur","un aventurier","le plombier","l'ingenieur gobelin","un vieux fou"]
second_var=["a glisse","a derape","a casse un bidule","a brise un truc","a vomi","a perdu ses clees","a fait ses besoins","etait bloque","s'est perdu","est tombe","s'est emdormi","a passe la nuit","s'est reveille","s'est tue","s'est fait mal","a trebuche","etait coince","s'est battu","a cause des ennuis","a mis le feu"]
second_fixed=" dans "
third_var=["la cave","le souterrain nord","le grenier","mon bureau","la remise a ingredient","les cuisines","la niche des chiens","la voliere a corbeaux","la fosse a scorpions","votre bureau","l'escalier du deuxieme niveau","le bac du limon glaireux","le couloir principal","le hangar de bricolage","l'atelier de forge","la salle de fouettage","le dortoir des orques","l'antre du Golbargh","le magasin","votre bibliotheque"]
third_fixed="\n ... et tout ca... a cause "
fourth_var=["de cette bete","de cette stupide","d'une grosse","d'une infame","d'une etrange","d'une incroyable","de l'improbable","de la fameuse","de cette imbecile de","de la ridicule",", c'est ballot, de la","de l'existance d'une","de l'embuche causee par une","du piege que representait une","de la presence de cette","vous allez rire, d'une","c'est bien dommage, de la","de la position d'une","de son penchant pour une","d'une mediocre"]
fifth_var=["brouette rouillee","manivelle tordue","scie abimee","bassine oubliee","cle de douze","corbeille de linge","hallebarde tordue","chouette empaillee","terrine piegee","flute empoisonnee","tete de goule","faux venimeuse","guitare disloquee","bielle biscornue","saliere brisee","peau de banane","perruque decrepite","chaussette rouge","babouche verte","pantoufle usee"]
fouth_fixed=" qui "
sixth_var=["venait de ma grand-mere","etait justement la","est apparue comme par magie","venait de votre cousin","avait ete abandonnee","etait suspecte","n'aurait pas du se trouver la","avait justement l'air fourbe","etait dans l'ombre","n'avait l'air de rien","a ete laissee par un voisin","etait bel et bien dangereuse","etait pourtant chere","avait une odeur inquietante","avait change de place","aurait du etre rangee","vous appartient","s'est revelee glissante","etait peut-etre a moi","pose toujours des problemes"]
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


