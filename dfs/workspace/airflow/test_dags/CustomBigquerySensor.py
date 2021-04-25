import datetime as dt
import sys
from datetime import datetime
from googleapiclient import errors
from airflow.operators.sensors import BaseSensorOperator
from airflow.utils.decorators import apply_defaults
import dmd_gap_setup





class Checktable():

    def table_exists(self,project_id, dataset_id, table_id):
        service = dmd_gap_setup.setup (None)
        try:
            service.tables ().get (
                projectId=project_id , datasetId=dataset_id ,
                tableId=table_id).execute ()
            return True
        except errors.HttpError as e:
            if e.resp['status'] == '404':
                return False
            raise


class CustomBigquerySensor(BaseSensorOperator):
    """
    Checks for the existence of a table in Google Bigquery.
    """
    template_fields = ('project_id', 'dataset_id', 'table_id',)
    ui_color = '#f0eee4'

    @apply_defaults
    @apply_defaults
    def __init__(
            self,
            project_id,
            dataset_id,
            table_id,
            delegate_to=None,
            *args,
            **kwargs):


        super (CustomBigquerySensor, self).__init__ (*args, **kwargs)
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id

    def poke(self, context):
        table_with_date_suffix = self.table_id + context.get ("ds_nodash")
        table_uri = '{0}:{1}.{2}'.format (self.project_id, self.dataset_id, table_with_date_suffix)
        print('Sensor checks existence of table: %s', table_uri)
        test_table = Checktable()
        return test_table.table_exists (self.project_id, self.dataset_id, table_with_date_suffix)


    # log is not working in 2.7

