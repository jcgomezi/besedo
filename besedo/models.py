from django.db import models



class contacts(models.Model):
    script_name = models.CharField(max_length=150, verbose_name='script_name')
    dataorigin_db = models.CharField(max_length=100, verbose_name='dataorigin_db')
    statistics_db = models.CharField(max_length=100, verbose_name='statistics_db')
    statistics_table = models.CharField(max_length=100, verbose_name='statistics_table')
    client_name = models.CharField(max_length=100, verbose_name='client_name')
    client= models.ForeignKey('EmailReportService.tb_clients',on_delete=models.CASCADE)
    script = models.OneToOneField('tbRPAs',primary_key=True,verbose_name='script',on_delete=models.CASCADE)
    sharedpaths = models.TextField( verbose_name='sharedpaths',null=True)
    remote_file_execution = models.CharField(max_length = 100, verbose_name='remote_file_execution')
    remote_server = models.CharField(max_length = 100, verbose_name='remote_server')
    language = models.CharField(max_length = 50, verbose_name='language')
    script_parameters = models.CharField(max_length = 100, verbose_name='script_parameters')
    def __str__(self):
        return '%s %s %s' % (self.client_name,self.script_id,self.script_name)

    class Meta():
        verbose_name = 'RPA service configuration'
        verbose_name_plural = 'RPA service configurations'
        db_table = 'tbRPAServiceConfigurations'
        ordering = ['script']