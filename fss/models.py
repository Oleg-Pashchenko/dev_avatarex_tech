from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=200, null=True)
    status = models.TextField(null=True)

    amocrm_host = models.TextField(null=True)
    amocrm_email = models.TextField(null=True)
    amocrm_password = models.TextField(null=True)

    work_mode = models.TextField(null=True)
    context = models.TextField(null=True)
    knowledge_data = models.JSONField(null=True)
    database_data = models.JSONField(null=True)
    qualification = models.JSONField(null=True)
    fields = models.JSONField(null=True, default=[])

    pipeline_id = models.JSONField(null=True)
    statuses_ids = models.JSONField(null=True)

    hi_message = models.TextField(null=True, default='Привет!')
    openai_error_message = models.TextField(null=True, default='Ошибка распознавания OpenAI!')
    database_error_message = models.TextField(null=True, default='Ошибка поиска в базе!')

    openai_api_token = models.TextField(null=True, default='')

    use_fields = models.BooleanField(null=True)
    use_voice = models.BooleanField(null=True)
    use_speak_with_manager = models.BooleanField(null=True)
    use_fine_tuned = models.BooleanField(null=True)

    database_perephrase_context = models.TextField(null=True)
    model_title = models.TextField(null=True)
    model_limit = models.IntegerField(null=True)
    max_tokens = models.IntegerField(null=True, default=1000)
    temperature = models.FloatField(null=True, default=1.0)
    fine_tuned_model_id = models.TextField(null=True)
    assistant_id = models.TextField(null=True)
    qualification_finish_message = models.TextField(null=True, default='')
    database_max_elements_count = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner_host}: {self.status}'
