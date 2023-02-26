from django.db import models

class Topic(models.Model) :
    tietle = models.CharField(max_length=200 , verbose_name=u"主题")
    time = models.DateTimeField(auto_now_add=True , verbose_name=u"添加的时间")

    def __str__(self) -> str:
        return f"{self.tietle}"
    
class Enty(models.Model):
    topic = models.ForeignKey(Topic , on_delete=models.CASCADE ,verbose_name=u"主题")
    body = models.TextField(verbose_name=u"正文")
    time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加的时间")

    class Meta :
        verbose_name_plural = "enties"

    def __str__(self) -> str:
        return f"{self.body[:50]}..."