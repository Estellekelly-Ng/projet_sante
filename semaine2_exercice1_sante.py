# AKEINI ACADEMI - Prijet Sante public
# Semaine 2 - Exercice 1 : Fiche Patient CHU Brazaville
# Votre nom : Estelle Kelly Nguefang
#date : 26 juin 2026

# --- SECTION 1: VARIABLES DU PATIENT
print ('=============================================')
nom_patient = 'MAWOUNGOU Celestine'
print ('FICHE PATIENT -', nom_patient)
print ('=============================================')
age_patient = (42)
print ('Age                  :', age_patient, 'ans')
sexe_patient = 'F'
print ('Sexe                 :', sexe_patient)
departement_patient = 'Brazaville'
print ('Departement          :', departement_patient)
couverture_sociale = 'CNSS'
print ('Couverture sociale   :', couverture_sociale)
#----SECTION 2 :  variable consultation
print ('--------------------------------------------')
print ('CONSULTATION')
type_consultation = "Urgences"
print('Type                 :', type_consultation)
cout_consultation_fcfa = (15000.0)
nb_consutations = (1)
remise_cnss_pct = (30.0)
diagnostic_principale = 'Paludisme grave'
print ('Diagnostic           :', diagnostic_principale)
print ('Cout unitaire        :', cout_consultation_fcfa, 'FCFA')
print ('Remise CNSS          :', remise_cnss_pct, "%" )
# cout total apres remise CNSS
cout_total_fcfa = cout_consultation_fcfa * (1- remise_cnss_pct/100)
print ('COUT TOTAL           :', cout_total_fcfa, 'FCFA')
print ('--------------------------------------------')
# --- SECTION 3 : VARIABLE HOPITAL ---
nom_hopital = 'CHU de Brazzaville'
ville_hopital = 'Brazaville'
nb_lits_total = (320)
nb_lits_occupes = (284)
nb_medecins_actifs = (47)
print ('HOPITAL              :', nom_hopital)
print ('Ville                :', ville_hopital)
pourcentage = nb_lits_occupes/nb_lits_total*100
print (f'Lits occupes         : {nb_lits_occupes} / {nb_lits_total} ({pourcentage : .1f}%)')
print ('Medecins actifs      :',nb_medecins_actifs)
nb_consultations_hopital = 120
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1)
print ('Ratio consult.       :', ratio_consultations_medecin, 'consultation / medecin ce matin')
print ('=============================================')
print('STATUT : Prise en charge validee')
print ('=============================================')