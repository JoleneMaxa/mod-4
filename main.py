
from google.cloud import bigquery
import os

from flask import Flask

app = Flask(__name__)


from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
tracer_provider = TracerProvider()
tracer_provider = BatchSpanProcessor(CloudTraceSpanExporter())
trace.set_tracer_provider(TracerProvider())


client = bigquery.Client()

# Perform a query.
QUERY=("""SELECT * FROM `mod-4-412623.jolene_dataset.predictions` LIMIT 10""")


@app.route("/")
def hello_world():
    """Example Hello World route."""
    rows = client.query_and_wait(QUERY)
    # rows = query_job.result()

    for row in rows:
        print(row[0])
    return print("this isn't working") 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


