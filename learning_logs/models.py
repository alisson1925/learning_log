from django.db import models


class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text    
    
class Entry(models.Model):
    """Algo específico aprendido sobre o assunto."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entrires'
    
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text[:50] + '...'
