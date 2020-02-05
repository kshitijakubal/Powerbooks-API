from flask import Flask, render_template, request,jsonify
from py2neo import Graph, Node, Relationship

app = Flask(__name__)

graph = Graph("http://localhost:11003/db/data")

# API to create godown nodes.
@app.route('/createGodown',methods=['POST'])
def createGodown():
    print(request.is_json)
    content = request.get_json()
    print(content)

    create_godown = """ 
    WITH {jsonobj} as v

    unwind v.PBXMLGodowns as val
    unwind val.PBXMLGodown as gg
    foreach (godown in gg| merge
    (godowns:Godowns
    {   
    name:godown.NAME,
    reservedname:godown.RESERVEDNAME,
    EXCISEREGISTRATIONDATE:godown.EXCISEREGISTRATIONDATE,
    PINCODE:godown.PINCODE,
    PHONENUMBER:godown.PHONENUMBER,
    EXCISERANGE:godown.EXCISERANGE,
    EXCISERANGEADDRESS:godown.EXCISERANGEADDRESS,
    EXCISEDIVISIONADDRESS:godown.EXCISEDIVISIONADDRESS,
    EXCISECOMMISSIONERATE:godown.EXCISECOMMISSIONERATE,
    EXCISERANGECODE:godown.EXCISERANGECODE,
    EXCISEDIVISIONCODE:godown.EXCISEDIVISIONCODE,
    PARENT:godown.PARENT,
    IMPORTEREXPORTERCODE:godown.IMPORTEREXPORTERCODE,
    EXCISEREGNO:godown.EXCISEREGNO,
    JOBNAME:godown.JOBNAME,
    EXCISEREGISTRATIONTYPE:godown.EXCISEREGISTRATIONTYPE,
    EXCISEMAILINGNAME:godown.EXCISEMAILINGNAME,
    EXCISEDIVISIONNAME:godown.EXCISEDIVISIONNAME,
    EXCISECOMSNRATECODE:godown.EXCISECOMSNRATECODE,
    EXCISECOMSNRATEADDRESS:godown.EXCISECOMSNRATEADDRESS,
    ARE1SERIALMASTER:godown.ARE1SERIALMASTER,
    ARE2SERIALMASTER:godown.ARE2SERIALMASTER,
    ARE3SERIALMASTER:godown.ARE3SERIALMASTER,
    TAXUNITNAME:godown.TAXUNITNAME,
    ISUPDATINGTARGETID:godown.ISUPDATINGTARGETID,
    ASORIGINAL:godown.ASORIGINAL,
    HASNOSPACE:godown.HASNOSPACE,
    HASNOSTOCK:godown.HASNOSTOCK,
    ISEXTERNAL:godown.ISEXTERNAL,
    ISINTERNAL:godown.ISINTERNAL,
    ENABLEEXPORT:godown.ENABLEEXPORT,
    ISPRIMARYEXCISEUNIT:godown.ISPRIMARYEXCISEUNIT,
    ALLOWEXPORTREBATE:godown.ALLOWEXPORTREBATE,
    ISTRADERRGNUMBERON:godown.ISTRADERRGNUMBERON,
    ALTERID:godown.ALTERID

    }
    )
    foreach(snl in  gg.SERIALNUMBERLIST | merge(godowns)-[:has]->(:SerialNumberList
    {EXCISEBOOKNAME:""})
    )
    foreach(lnl in  gg.LANGUAGENAMELIST | merge(godowns)-[:has]->(:LanguageNameList
    {SCHVIDETAILS:""})

    )
    )
    """

    graph.run(create_godown,jsonobj=content)
    return "Godown created successfully"

# API to edit Godown Details.
@app.route('/editGodownDetails',methods=['POST'])
def editGodownDetails():
    print(request.is_json)
    content = request.get_json()
    print(content)

    name = request.args['name']

    edit_godown_details = """ 
    WITH {jsonobj} as v

    MATCH(godowns:Godowns)
    unwind v.PBXMLGodowns as val
    unwind val.PBXMLGodown as gg
    WHERE godown.name={NAME}
    foreach (godown in gg| SET godown.name=godowns.name,
    reservedname:godowns.RESERVEDNAME,
    EXCISEREGISTRATIONDATE:godowns.EXCISEREGISTRATIONDATE,
    PINCODE:godowns.PINCODE,
    PHONENUMBER:godowns.PHONENUMBER,
    EXCISERANGE:godowns.EXCISERANGE,
    EXCISERANGEADDRESS:godowns.EXCISERANGEADDRESS,
    EXCISEDIVISIONADDRESS:godowns.EXCISEDIVISIONADDRESS,
    EXCISECOMMISSIONERATE:godowns.EXCISECOMMISSIONERATE,
    EXCISERANGECODE:godowns.EXCISERANGECODE,
    EXCISEDIVISIONCODE:godowns.EXCISEDIVISIONCODE,
    PARENT:godowns.PARENT,
    IMPORTEREXPORTERCODE:godowns.IMPORTEREXPORTERCODE,
    EXCISEREGNO:godowns.EXCISEREGNO,
    JOBNAME:godowns.JOBNAME,
    EXCISEREGISTRATIONTYPE:godowns.EXCISEREGISTRATIONTYPE,
    EXCISEMAILINGNAME:godowns.EXCISEMAILINGNAME,
    EXCISEDIVISIONNAME:godowns.EXCISEDIVISIONNAME,
    EXCISECOMSNRATECODE:godowns.EXCISECOMSNRATECODE,
    EXCISECOMSNRATEADDRESS:godowns.EXCISECOMSNRATEADDRESS,
    ARE1SERIALMASTER:godowns.ARE1SERIALMASTER,
    ARE2SERIALMASTER:godowns.ARE2SERIALMASTER,
    ARE3SERIALMASTER:godowns.ARE3SERIALMASTER,
    TAXUNITNAME:godowns.TAXUNITNAME,
    ISUPDATINGTARGETID:godowns.ISUPDATINGTARGETID,
    ASORIGINAL:godowns.ASORIGINAL,
    HASNOSPACE:godowns.HASNOSPACE,
    HASNOSTOCK:godowns.HASNOSTOCK,
    ISEXTERNAL:godowns.ISEXTERNAL,
    ISINTERNAL:godowns.ISINTERNAL,
    ENABLEEXPORT:godowns.ENABLEEXPORT,
    ISPRIMARYEXCISEUNIT:godowns.ISPRIMARYEXCISEUNIT,
    ALLOWEXPORTREBATE:godowns.ALLOWEXPORTREBATE,
    ISTRADERRGNUMBERON:godowns.ISTRADERRGNUMBERON,
    ALTERID:godowns.ALTERID
    """

# API to delete Godown
@app.route('/deleteGodown',methods=['GET'])
def deleteGodown():

    name = request.args['name']

    delete_godown = """ 
    MATCH(godown:Godowns)
    WHERE godown.name={NAME}
    DETACH DELETE godown
    """
    graph.run(delete_godown,NAME=name)
    return "Godown deleted successfully"

# API to get Godown details
@app.route('/getGodownDetails',methods=['GET'])
def getGodownDetails():
    name = request.args['name']

    get_godown_details = """ 
    MATCH(godown:Godowns)
    where godown.name = {NAME}
    return godown
    """
    result = jsonify(graph.run(get_godown_details,NAME=name).data())
    return result

# API to get all Godown details
@app.route('/getAllGodown',methods=['GET'])
def getAllGodown():

    get_all_godowns = """
    match(godown:Godowns)  
    RETURN godown
    """

    result = []
    for res in graph.run(get_all_godowns):
        result.append(str(res[0]))

    return jsonify(result)




app.run(host='127.0.0.1', port=5000)