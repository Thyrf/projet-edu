# Lien avec l'apprentissage autonome

Revenons à l'exemple donné en introduction:
Comment utiliser une stratégie similaire à celle de l'activité robotique pour ajuster les paramètres d'un réseau de neurone ?

Il faut un objectif quantitatif, souvent appelé une fonction de coût. Dans l'activité robotique celle-ci était définie par l'illumination moyenne perçue par les 4 capteurs que l'on cherchait à maximiser. Dans l'exemple avec les images de chiffres, nous utiliserons une collection d'image de chiffre avec la sortie du réseau de neurones que l'on souhaiterait avoir. Cette collection de paires d'échantillons (entrée -> sortie désirée) est appellée **ensemble d'entrainement** ou *training set*. La fonction de coût est définie comme la somme des erreurs entre la sortie effective pour les échantillons du training set et la sortie désirée.

Il faut en plus de cela savoir comment la fonction de coût varie lorsque l'on change les paramètres. Dans l'activité de robotique cela correspond à *diff*, la différence de mesure entre les capteurs. Dans l'exemple et dans la plupart des applications d'apprentissage autonome, cela sera obtenu grâce à la dérivée de la fonction de coût en fonction des paramètres. La dérivée est un outils mathématique qui sera étudiée au gymnase et qui sera utilisée en cours de physique. 

