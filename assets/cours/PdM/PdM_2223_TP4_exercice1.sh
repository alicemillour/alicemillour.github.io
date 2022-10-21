#!/bin/sh

# Question 3
wget https://www.data.gouv.fr/fr/ datasets/r/b363e051-9649-4879-ae78-71ef227d0cc5

# Question 4
mv b363e051-9649-4879-ae78-71ef227d0cc5 base_de_donnees.csv

# Question 6
head -n 1 base_de_donnees.csv > en_tete.txt
cat en_tete.txt

# Question 7
# nb lignes (102):
cat en_tete.txt | wc -l
# écriture
tail -n 101 base_de_donnees.csv > corps.csv

# autre option plus compacte :
tail -n $((`cat base_de_donnees.csv | wc -l`-1)) base_de_donnees.csv > corps.csv

# Question 8 : on trie et on repère la ligne où le département passe à 30 (ligne 31)
sort -t',' -k4 corps.csv | grep -n 30
head -n 30 corps.csv > dep_inf_30.csv

# on récupère les académies de la zone A
cat corps.csv | grep "Zone A" > zone_A.csv

# La commande 'comm' ne peux comparer que des fichiers qui sont classés dans le même ordre car la comparaison se fait ligne par ligne. Par conséquent il faut trier les deux fichiers avant de pouvoir les comparer.

sort zone_A.csv > zone_A_trie.csv
sort dep_inf_30.csv > dep_inf_30_trie.csv

# on obtient les lignes des académies dont le département est inférieur à 30 ne se trouvant pas en zone A avec par exemple :
comm -2 -2 dep_inf_30_trie.csv zone_A_trie.csv 


# Question 9
cat corps.csv | cut -d',' -f1 | sed "s/Académie d'//" | sed "s/Académie de //" | sort -f > toponymes.txt

# Question 10 
echo "Zone A" > zones.txt
echo "Zone B" >> zones.txt
echo "Zone C" >> zones.txt

cat corps.csv | grep "Zone A" | wc -l > compte.txt
cat corps.csv | grep "Zone B" | wc -l >> compte.txt
cat corps.csv | grep "Zone C" | wc -l >> compte.txt

paste zones.txt compte.txt > zone_compte.txt
