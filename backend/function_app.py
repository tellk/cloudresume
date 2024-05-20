import azure.functions as func
import json
import logging

app = func.FunctionApp()

@app.function_name(name="main")
@app.route(route="read-items/webpage01")
@app.cosmos_db_input(arg_name="items",
                     database_name='WebMetricsDb', 
                     container_name='PageViews',
                     connection='CosmosDbConnectionSetting',
                     sql_query='SELECT * FROM c WHERE c.id = "webpage01"')
@app.cosmos_db_output(arg_name='outputDocument', 
                      database_name='WebMetricsDb', 
                      container_name='PageViews',
                      connection='CosmosDbConnectionSetting')



def increment_view_count(req: func.HttpRequest, items: func.DocumentList, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    # Set up logging
    logging.info('Function CosmosDBExample triggered with ID: webpage01')
    
    if not items:
        logging.warning('Document with ID webpage01 not found')
        return func.HttpResponse('Document not found', status_code=404)
    
    # Increment the viewCount attribute
    document = items[0]
    document['viewCount'] = document.get('viewCount', 0) + 1
    
    # Use the output binding to save the updated document
    outputDocument.set(document)
    
    logging.info('viewCount incremented and document updated in the database')
    logging.info(f"Document with ID webpage01 has viewCount: {document['viewCount']}")
    return func.HttpResponse(f"Updated document viewCount to {document['viewCount']}", mimetype="text/plain")