import httpx
import os

LS_HOST = os.environ.get('LS_API_HOST', 'localhost')
LS_PORT = os.environ.get('LS_API_PORT', '9600')

class PipelineInfo:
    # API request on pipelines and further filter down on a specific pipeline, see:
    # https://www.elastic.co/guide/en/logstash/current/node-stats-api.html#pipeline-stats

    def __init__(self, pipeline='main', host=LS_HOST, port=LS_PORT) -> None:
        self.pipeline = pipeline
        self.host = host
        self.port = port

    def get_info(self):
        res = httpx.get(f'http://{self.host}:{self.port}/_node/stats/pipelines?pretty')
        data = res.json()
        info = data['pipelines'][self.pipeline]
        return info

    def get_events(self):
        return self.get_info()['events']

    def get_flow_info(self, kind: str):
        return self.get_info()['flow'][kind]

    def get_filters_info(self):
        return self.get_info()['plugins']['filters']

    def get_inputs_info(self):
        return self.get_info()['plugins']['inputs']

print(PipelineInfo().get_inputs_info())
