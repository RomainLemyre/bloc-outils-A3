==============
bloc-outils-A3
==============

I) Copiez l'ensemble des fichiers dans votre répertoire de travail python.


II) Pour importer l'ensemble des fonctions/classes dans vos script:
>> from bloc_outils import *

Pour importer une fonction/classe en particulier:
>> from bloc_outils import NomDeLaFonction

III) Pour utiliser une fonction:
>> y = NomDeLaFonction(x0, ..., xn)
avec : y équivalent à la sortie du bloc simulink
       x0,...,xn équivalent aux entrées du bloc simulink

IV) Pour utiliser une classe:
>> instanceDeClasse = NomDeLaClasse(p0, ..., pn)
>> instanceDeClasse.execute(x0, ..., xn)
>> y = instanceDeClasse.output
avec : y équivalent à la sortie du bloc simulink
       x0,...,xn équivalent aux entrées du bloc simulink
       p0,...,pn équivalent aux paramètres du bloc simulink


* Les noms des fichiers sont identiques aux noms des fonctions/classes qu'ils contiennent.
