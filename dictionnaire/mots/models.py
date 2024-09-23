from django.db import models

class Mot(models.Model):
    # Mot dans la langue Sar
    mot_sar = models.CharField(max_length=100)
    # Traduction française
    mot_fr = models.CharField(max_length=100)
    # Type de mot (nom, adjectif, verbe, etc.)
    type_mot = models.CharField(max_length=50)
    # Phrase d'exemple dans la langue Sar
    phrase_sar = models.TextField()
    # Traduction de la phrase en français
    phrase_fr = models.TextField()

    def __str__(self):
        return self.mot_sar
