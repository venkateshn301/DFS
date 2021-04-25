import logging

from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults

log = logging.getLogger(__name__)

class SampleOperator(BaseOperator):

    @apply_defaults
    def __init__(self, my_operator_param, *args, **kwargs):
        self.operator_param = my_operator_param
        super(SampleOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info("Hello from Sample Operator!")
        log.info('operator_param: %s', self.operator_param)

class SamplePlugin(AirflowPlugin):
    name = "sample plugin"
    operators = [SampleOperator]
