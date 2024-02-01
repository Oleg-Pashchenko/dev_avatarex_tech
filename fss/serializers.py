from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 'text', 'status',
            'amocrm_host', 'amocrm_email', 'amocrm_password',
            'work_mode', 'context', 'knowledge_data', 'database_data',
            'qualification', 'fields', 'pipeline_id', 'statuses_ids',
            'hi_message', 'openai_error_message', 'database_error_message',
            'openai_api_token', 'use_fields', 'use_voice',
            'use_speak_with_manager', 'use_fine_tuned', 'database_perephrase_context',
            'model_title', 'model_limit', 'max_tokens', 'temperature',
            'fine_tuned_model_id', 'assistant_id', 'qualification_finish_message',
            'database_max_elements_count', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'fields': {'default': []},
            'hi_message': {'default': 'Привет!'},
            'openai_error_message': {'default': 'Ошибка распознавания OpenAI!'},
            'database_error_message': {'default': 'Ошибка поиска в базе!'},
            'openai_api_token': {'default': ''},
            'max_tokens': {'default': 1000},
            'temperature': {'default': 1.0},
            'qualification_finish_message': {'default': ''}
        }
