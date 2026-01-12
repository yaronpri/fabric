import datetime
import fabric.functions as fn
import logging

udf = fn.UserDataFunctions()

@udf.connection(argName="varLib", alias="demoVL")
@udf.function()
def hello_fabric(name: str, varLib: fn.FabricVariablesClient) -> str:
    logging.info('Python UDF trigger function processed a request.')

    variables = varLib.getVariables()
    notebookV = variables.get("notebookVariable")
    return f"Welcome to Fabric Functions, {name}, value of var= {notebookV} at {datetime.datetime.now()}!"


