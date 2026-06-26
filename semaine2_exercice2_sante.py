# ======================================================
# AKEINI ACADEMY - Projet Sante Public
# Semaine 2 - Exercice 2 KPIs Sanitairezs OMS
# ======================================================
# ---- données brutes----
budget_fcfa          = (87_450_000) #underscore pour lisibilité des grands nombres
nb_consultations_ext = 4823
nb_hospitalisations  = 1247
nb_deces             = 18
nb_lits_total        = 180
nb_lits_occupes      = 143
nb_medecin           = 22
nb_infirmier         = 58
population_dept      = 128_000
taux_eur_fcfa        = 655.951
taux_usd_fcfa        = 600.0

#conversion dévise
budget_eur = round(budget_fcfa / taux_eur_fcfa, 2)
budget_usd = round(budget_fcfa / taux_usd_fcfa, 2)

# 2. Indicateurs OMS
densite_medicale = round((nb_medecin/population_dept) * 1000, 1)
taux_mortalité   = round((nb_deces/nb_hospitalisations) * 100, 1)
taux_occupation  = round((nb_lits_occupes / nb_lits_total) * 100, 1)

# 3. Division entiere et modulo
budget_medicaments   = int (budget_fcfa* 0.35)
cout_journalier_meds = 450_000
jours_stock          = budget_medicaments // cout_journalier_meds  # division entiere
jours_restants       = budget_medicaments % cout_journalier_meds  # modulo %

# 4. Puissance pour projection
budget_n_plus_2      = round(budget_fcfa* (1.08**2), 1)

# ---- AFFICHAGE RAPPORT ----
print (f'=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-noire ===')
print ('  DEpense Q4        :', budget_fcfa, 'FCFA')
print ('  En euros          :', budget_eur, 'EUR')
print ('  En dollars        :', budget_usd, 'USD')
print ('INDICATEURS OMS')
print ('  Densite medicale  :', densite_medicale, 'medecins/ 1000 ha  [norme OMS >= 2.3]')
print ('  Taux de mortalité  :', taux_mortalité,                      '[Seuil alerte : > 2%]')
print ('  Taux occupation   :', taux_occupation,                     '[optimal : 70-85%]')
print ('ANALYSE PHARMACIE')
print ('  Budget medicaments:', budget_medicaments, 'FCFA')
print ('  Jours de stock    :', jours_stock, 'jours')
print ('  Jours depassement :', jours_restants, 'jours')
print ('PROJECTION')
print ('budget N+2 (8%/an)  :',budget_n_plus_2, 'FCFA')
print ('ALERTE : densite medicale CRITIQUE (0.2 pour 1000 hab - norme OMS : 2.3)')
