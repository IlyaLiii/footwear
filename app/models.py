from django.db import models

class Snikers(models.Model):
    # get_SNIKER_SIZE_display() чтобы взять второе значение тупла)
    SNIKER_SIZE = (
        ('45', '45 EU'),
        ('46', '46 EU'),
        ('47', '47 EU'),
        ('48', '48 EU'),
    )
    company = models.CharField(max_length=100, null=True, db_index=True)
    model = models.CharField(max_length=100, null=True, db_index=True)
    size = models.CharField(max_length=20, choices=SNIKER_SIZE, null=True)
    price = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "snikers"
        verbose_name = "sniker"
        verbose_name_plural = "snikers"

    def __str__(self):
        return '%s %s' % (self.company, self.model)



# TODO:Переобозначить метод delete(), чтобы можно было восстановить из дб , в случае случайного удаления ( меняем deleted = True )

#    def delete(self, *args, **kwargs):

    @property
    def full_name(self):
        "Return name of company + model"
        return '%s %s' % (self.company, self.model)


class Choice(models.Model):
    Snikers = models.ForeignKey(Snikers, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        db_table = "choice"

    def __str__(self):
        return self.choice_text


