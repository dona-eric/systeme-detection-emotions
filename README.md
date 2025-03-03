# Projet: Système de Reconnaissance d'Émotions en Temps Réel.

### **Intelligence Emotionnelle 😮‍💨😮‍💨**

### *** Santé Mentale des élèves et étudiants ***
     Dans une salle de cours ultra-moderne, Dona observait les écrans de surveillance de l'école CSP Mandela.Curieux 🤔, il affirme: Ce n’était pas un simple agent 🤔!. Il travaillait sur un projet ambitieux : un système de reconnaissance d’émotions capable de détecter les comportements suspects et d’améliorer l’expérience des clients et des élèves.  
    Ce jour-là, Dona aperçu un de ses camarades qui errait entre les rayons de la cours de l'école. Son regard inquiet et ses gestes nerveux attirèrent l’attention du système. L’algorithme analysa l'expression sur son visage et détecta une anxiété anormale 😱. Était-ce un simple stress ou un signe précurseur d’un acte dangereux ou un manque de sommeil ?  
    Quelques instants plus tard, une alerte s’afficha sur l’écran du directeur : **"Niveau d’anxiété élevé 😱 – Risque potentiel."** Le directeur, intrigué 😣, envoya discrètement un agent  de secous sur place. À peine arrivé, l’agent vit le camarade de Dona s’effondrer. Il souffrait d’une crise de panique. Pourquoi ?? Parcequ'il avait peur qu'après la récréation son directeur ne puisse le fouéter pour léçon non apprise et examen blanc non reussit 🤣. 
    Grâce à l’alerte, les secours furent appelés immédiatement, lui sauvant la vie(finalement on l'a fouété  le lendemain 🤣).  
### *** Dans le secteur Commercial ***

    Dans un supermarché de ventes des divers et des bouffes,une cliente du nom de Moni vint pour des achats mais à sa grande surprise, elle ne decouvrit pas ceux pourquoi elle était de le supermarket. Heureusement, le système de Dona fut installé et identifia que Moni etait frustrée. Son visage crispé, ses sourcils froncés… Elle semblait agacée par un service. Une notification fut envoyée aux employés, qui lui proposèrent immédiatement de l’aide. Surprise par cette attention, son visage s’illumina. Elle sourit et continua ses achats.  Gain de cause 🤩 , elle est satisfaite 🤩.
Alors ce système qu'est il ? Et comment l'utiliser ?

😊😊😊 Je vous présente  **EMOTISCAN**

***EMOTISCAN*** : 
               est un outil qui identifie l'émotions ou l'hummeur des individus, des clients et ou des patients en temps réel. Ce n'est pas seulement une application                     web mais un système capable de détecter ou reconnaitre l'émotions qu'anime un individus(dans votre restaurant), un client(dans votre supermarket) , un                     patient(dans votre centre de santé ou dans votre centre theurapeutique)en temps réel. Ce système, d’abord conçu pour la sécurité, est bien plus qu'un                      atout majeur dans bien d’autres domaines : le marketing, la santé, la psychologie, l'éducation. Il peut détecter le mal-être des patients dans un                          hôpital, améliorer les interactions en ligne ou prévenir des incidents dans les espaces publics.  

**Objectif**: Développer un système de reconnaissance d'émotions en temps réel et intégration dans une application Web
      Un outil capable d’analyser les émotions en temps réel via une simple webcam, avec un modèle d’IA puissant pour interpréter les expressions faciales avec précision.

**Développement**

### 🚀 **Plan du projet :**  
1️⃣ **Préparation des données et du modèle**  
   - Utiliser un modèle pré-entraîné (**DeepFace**, **FER2013**, ou un CNN personnalisé avec TensorFlow/PyTorch).  
   - Tester la détection des émotions sur des images et en vidéo avec **OpenCV**.  

2️⃣ **Création de l’application Django**  
   - Configurer Django et Django REST Framework pour gérer les API.  
   - Définir un modèle pour stocker les résultats d’analyse (émotion, timestamp, etc.).  

3️⃣ **Capture vidéo en temps réel avec OpenCV**  
   - Intégrer OpenCV pour capturer le flux de la webcam.  
   - Détecter les visages et prédire les émotions.  

4️⃣ **Affichage des résultats sur Django avec WebSockets**  
   - Utiliser **Django Channels** pour transmettre les émotions en temps réel.  
   - Mettre à jour l’interface utilisateur dynamiquement avec **JavaScript (AJAX ou WebSockets)**.  

5️⃣ **Déploiement de l’application**  
   - Héberger l’API Django (Render, Railway, AWS).  
   - Utiliser **Docker** et **NGINX** si nécessaire pour le streaming vidéo.  

**NB**: Ce projet est encore en cours d'amélioration et de reviser de code. Les premiers tests ne satisfaient pas encore les conditions d'utilisations.
