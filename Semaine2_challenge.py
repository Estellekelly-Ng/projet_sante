# AKEINI ACADEMY - Challenge


# SECTION 1 : declaration des variables
# H1 Hopital District Kinkala
k_nom                  = 'Hopital District Kinkala'
k_budget_trimestre     = 12_500_000
k_consultations_ext    = 1_847
k_hospitalisation      = 312
k_deces_hospitaliers   = 8
k_lits_totaux          = 45
k_lits_occupes         = 41
K_medecins_permanant   = 3
k_population_desservie = 85_000

# H2 CMS de Vindza
v_nom                  = 'CMS de Vindza'
v_budget_trimestre     = 6_800_000
v_consultations_ext    = 923
v_hospitalisation      = 87
v_deces_hospitaliers   = 2
v_lits_totaux          = 20
v_lits_occupes         = 14
v_medecins_permanant   = 1
v_population_desservie = 42_000

# H3 hopitalcde Kindamba
ki_nom                  = 'Hopital de Kindamba'
ki_budget_trimestre     = 9_200_000
ki_consultations_ext    = 1_234
ki_hospitalisation      = 201
ki_deces_hospitaliers   = 11
ki_lits_totaux          = 35
ki_lits_occupes         = 33
ki_medecins_permanant   = 2
ki_population_desservie = 42_000

# SECTION 2 : calcul des KPI de chaque hoptal
# # formules utilisées
# cout moyen par patient = budget/consultation externes
# taux d'occupation = lits occupés/lits totaux * 100
# densité medicale = nb de medecin / pop * 1000
# taux de mortalité = nb de deces/ hospitalisations * 100

# H1 Hopital District Kinkala
k_cout_moyen       = round(k_budget_trimestre / k_consultations_ext, 2) 
k_taux_occupation  = round(k_lits_occupes/k_lits_totaux * 100, 2)
k_densite          = round(K_medecins_permanant/k_population_desservie * 1000,2)
k_mortalite        = round(k_deces_hospitaliers/k_hospitalisation * 100, 1)

# H2 CMS de Vindza
v_cout_moyen       = round(v_budget_trimestre/v_consultations_ext)
v_taux_occupation  = round(v_lits_occupes/v_lits_totaux * 100, 2)
v_densite          = round(v_medecins_permanant/v_population_desservie * 1000, 2)
v_mortalite        = round(v_deces_hospitaliers/v_hospitalisation * 100, 1)

# H3 hopital de Kindamba
ki_cout_moyen      = round(ki_budget_trimestre/ki_consultations_ext, 2)
ki_taux_occupation = round(ki_lits_occupes/ki_lits_totaux * 100, 2)
ki_densite         = round(ki_medecins_permanant/ki_population_desservie * 1000, 2)
ki_mortalite       = round(ki_deces_hospitaliers/ki_hospitalisation * 100, 1)

# SECTION 3 : identification des hopitaux en situation de crise
# pour qu'un hopital soit en situation critique : taux mortalite > 2% OU densite < 0.05
if k_mortalite > 2.0 or k_densite < 0.05:
    statut_k_mortalite = ' CRITIQUE'
else:
    statut_k_mortalite = 'Ok'
if v_mortalite > 2.0 or k_densite < 0.05:
    statut_v_mortalite = ' CRITIQUE'
else:
    statut_v_mortalite = 'Ok'
if ki_mortalite > 2.0 or k_densite < 0.05:
    statut_ki_mortalite = ' CRITIQUE'
else:
    statut_ki_mortalite = 'OK'

# SZECTION 4 : bonus
cout_medecin_trimestre  = 1_200_000     # en FCFA 
medecins_cible          = 5             # nb de medecin qu'on veut avoir
 
# Combien de medecins manquent-il dans chaque hopital ?
k_medecins_manquants   = medecins_cible - K_medecins_permanant 
v_medecins_manquants   = medecins_cible - v_medecins_permanant  
ki_medecins_manquants  = medecins_cible - ki_medecins_permanant 
 
# Cout total pour embaucher les medecins manquants
cout_recrutement_total = (
    k_medecins_manquants +
    v_medecins_manquants  +
    ki_medecins_manquants
) * cout_medecin_trimestre
 
# Budget total disponible pour les trois hopitaux sont :
budget_total = k_budget_trimestre + v_budget_trimestre + ki_budget_trimestre
 
if budget_total >= cout_recrutement_total:
    budget_statut = 'OUI, budget suffisant'
else:
    budget_statut = 'NON, budget insuffisant'

# PRESENTATION
print('=*60')
print('---rapport comparatif des trois hopitaux du departement du Pool---')
print('Date : 8 janvier 2026')
print('=*60')

print(f'{'VARIABLES':<28} {k_nom:>10,} {v_nom:>10,} {ki_nom:>10}')
print(f'{'Budget'} {k_budget_trimestre:>10} {v_budget_trimestre:>10} {ki_budget_trimestre:>10}')
print(f'{'Consultation externe:<28}'} {k_consultations_ext:>10} {v_consultations_ext} {ki_consultations_ext}')
print(f'{'Hospitalisation:<28}'} {k_hospitalisation::>10} {v_hospitalisation:>10} {ki_hospitalisation:>10}')
print(f'{'Deces hospitalier'} {k_deces_hospitaliers:>10} {v_deces_hospitaliers:>10} {ki_deces_hospitaliers:>10}')
print(f'{'Lits totaux'} {k_lits_totaux:>10} {v_lits_totaux:>10} {ki_lits_totaux:>10}')
print(f'{'Lits occupes'} {k_lits_occupes:>10} {v_lits_occupes:>10} {ki_lits_occupes:>10}')
print(f'{'Medecins permanents'} {ki_medecins_permanant:>10} {v_medecins_permanant:>10} {ki_medecins_permanant:>10}')
print(f'{'Population'} {k_population_desservie:>10} {v_population_desservie:>10} {ki_population_desservie:>10}')
print('-*60')
print('KPIs')
print(f'{'Cout moyen/patient (en FCFA)'} {k_cout_moyen:>10} {v_cout_moyen:>10} {ki_cout_moyen:>10}')
print(f'{'Taux occupation lit (%)'} {ki_taux_occupation:>10} {v_taux_occupation:>10} {ki_taux_occupation:>10}')
print(f'{'Densite medicale'} {k_densite:>10} {v_densite:>10} {ki_densite:>10}')
print(f'{'Taux de mortalite (%)'} {k_mortalite:>10} {v_mortalite:>10} {ki_mortalite:>10}')
print('-*60')
print('---STATUT---')
print(f'{'statut'} {statut_k_mortalite:>10} {statut_v_mortalite:>10} {statut_ki_mortalite:>10}')

# AKEINI ACADEMY - Challenge


# SECTION 1 : declaration des variables
# H1 Hopital District Kinkala
k_nom                  = 'Hopital District Kinkala'
k_budget_trimestre     = 12_500_000
k_consultations_ext    = 1_847
k_hospitalisation      = 312
k_deces_hospitaliers   = 8
k_lits_totaux          = 45
k_lits_occupes         = 41
K_medecins_permanant   = 3
k_population_desservie = 85_000

# H2 CMS de Vindza
v_nom                  = 'CMS de Vindza'
v_budget_trimestre     = 6_800_000
v_consultations_ext    = 923
v_hospitalisation      = 87
v_deces_hospitaliers   = 2
v_lits_totaux          = 20
v_lits_occupes         = 14
v_medecins_permanant   = 1
v_population_desservie = 42_000

# H3 hopitalcde Kindamba
ki_nom                  = 'Hopital de Kindamba'
ki_budget_trimestre     = 9_200_000
ki_consultations_ext    = 1_234
ki_hospitalisation      = 201
ki_deces_hospitaliers   = 11
ki_lits_totaux          = 35
ki_lits_occupes         = 33
ki_medecins_permanant   = 2
ki_population_desservie = 42_000

# SECTION 2 : calcul des KPI de chaque hoptal
# # formules utilisées
# cout moyen par patient = budget/consultation externes
# taux d'occupation = lits occupés/lits totaux * 100
# densité medicale = nb de medecin / pop * 1000
# taux de mortalité = nb de deces/ hospitalisations * 100

# H1 Hopital District Kinkala
k_cout_moyen       = round(k_budget_trimestre / k_consultations_ext, 2) 
k_taux_occupation  = round(k_lits_occupes/k_lits_totaux * 100, 2)
k_densite          = round(K_medecins_permanant/k_population_desservie * 1000,2)
k_mortalite        = round(k_deces_hospitaliers/k_hospitalisation * 100, 1)

# H2 CMS de Vindza
v_cout_moyen       = round(v_budget_trimestre/v_consultations_ext)
v_taux_occupation  = round(v_lits_occupes/v_lits_totaux * 100, 2)
v_densite          = round(v_medecins_permanant/v_population_desservie * 1000, 2)
v_mortalite        = round(v_deces_hospitaliers/v_hospitalisation * 100, 1)

# H3 hopital de Kindamba
ki_cout_moyen      = round(ki_budget_trimestre/ki_consultations_ext, 2)
ki_taux_occupation = round(ki_lits_occupes/ki_lits_totaux * 100, 2)
ki_densite         = round(ki_medecins_permanant/ki_population_desservie * 1000, 2)
ki_mortalite       = round(ki_deces_hospitaliers/ki_hospitalisation * 100, 1)

# SECTION 3 : identification des hopitaux en situation de crise
# pour qu'un hopital soit en situation critique : taux mortalite > 2% OU densite < 0.05
if k_mortalite > 2.0 or k_densite < 0.05:
    statut_k_mortalite = ' CRITIQUE'
else:
    statut_k_mortalite = 'Ok'
if v_mortalite > 2.0 or k_densite < 0.05:
    statut_v_mortalite = ' CRITIQUE'
else:
    statut_v_mortalite = 'Ok'
if ki_mortalite > 2.0 or k_densite < 0.05:
    statut_ki_mortalite = ' CRITIQUE'
else:
    statut_ki_mortalite = 'OK'

# SZECTION 4 : bonus
cout_medecin_trimestre  = 1_200_000     # en FCFA 
medecins_cible          = 5             # nb de medecin qu'on veut avoir
 
# Combien de medecins manquent-il dans chaque hopital ?
k_medecins_manquants   = medecins_cible - K_medecins_permanant 
v_medecins_manquants   = medecins_cible - v_medecins_permanant  
ki_medecins_manquants  = medecins_cible - ki_medecins_permanant 
 
# Cout total pour embaucher les medecins manquants
cout_recrutement_total = (
    k_medecins_manquants +
    v_medecins_manquants  +
    ki_medecins_manquants
) * cout_medecin_trimestre
 
# Budget total disponible pour les trois hopitaux sont :
budget_total = k_budget_trimestre + v_budget_trimestre + ki_budget_trimestre
 
if budget_total >= cout_recrutement_total:
    budget_statut = 'OUI, budget suffisant'
else:
    budget_statut = 'NON, budget insuffisant'

# PRESENTATION
print('=*60')
print('---rapport comparatif des trois hopitaux du departement du Pool---')
print('Date : 8 janvier 2026')
print('=*60')

print(f'{'VARIABLES':<28} {k_nom:>10,} {v_nom:>10,} {ki_nom:>10}')
print(f'{'Budget'} {k_budget_trimestre:>10} {v_budget_trimestre:>10} {ki_budget_trimestre:>10}')
print(f'{'Consultation externe:<28}'} {k_consultations_ext:>10} {v_consultations_ext} {ki_consultations_ext}')
print(f'{'Hospitalisation:<28}'} {k_hospitalisation::>10} {v_hospitalisation:>10} {ki_hospitalisation:>10}')
print(f'{'Deces hospitalier'} {k_deces_hospitaliers:>10} {v_deces_hospitaliers:>10} {ki_deces_hospitaliers:>10}')
print(f'{'Lits totaux'} {k_lits_totaux:>10} {v_lits_totaux:>10} {ki_lits_totaux:>10}')
print(f'{'Lits occupes'} {k_lits_occupes:>10} {v_lits_occupes:>10} {ki_lits_occupes:>10}')
print(f'{'Medecins permanents'} {ki_medecins_permanant:>10} {v_medecins_permanant:>10} {ki_medecins_permanant:>10}')
print(f'{'Population'} {k_population_desservie:>10} {v_population_desservie:>10} {ki_population_desservie:>10}')
print('-*60')
print('KPIs')
print(f'{'Cout moyen/patient (en FCFA)'} {k_cout_moyen:>10} {v_cout_moyen:>10} {ki_cout_moyen:>10}')
print(f'{'Taux occupation lit (%)'} {ki_taux_occupation:>10} {v_taux_occupation:>10} {ki_taux_occupation:>10}')
print(f'{'Densite medicale'} {k_densite:>10} {v_densite:>10} {ki_densite:>10}')
print(f'{'Taux de mortalite (%)'} {k_mortalite:>10} {v_mortalite:>10} {ki_mortalite:>10}')
print('-*60')
print('---STATUT---')
print(f'{'statut'} {statut_k_mortalite:>10} {statut_v_mortalite:>10} {statut_ki_mortalite:>10}')
