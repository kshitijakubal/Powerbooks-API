from flask import Flask, render_template, request,jsonify
from py2neo import Graph, Node, Relationship

app = Flask(__name__)

graph = Graph("http://localhost:7474/db/data")

# API to create Stock Item Nodes
@app.route('/AddSPBXMLStockItems',methods=['POST'])
def AddSPBXMLStockItems():
    print(request.is_json)
    content = request.get_json()
    print(content)

    create_stockitem = """
    WITH {jsonobj} as v

    create(c:comp)
    with c, v.PBXMLStockItems as vl

    unwind vl as val
    unwind val.PBXMLStockItem as st

    with c, val, st
    foreach (stockitem in st| merge
    (stockitems:StockItems
    {
    NAME:stockitem.NAME,
    GUID:stockitem.GUID,
    CATEGORY:stockitem.CATEGORY,
    GSTAPPLICABLE:stockitem.GSTAPPLICABLE,
    TAXCLASSIFICATIONNAME:stockitem.TAXCLASSIFICATIONNAME,
    GSTTYPEOFSUPPLY:stockitem.GSTTYPEOFSUPPLY,
    EXCISEAPPLICABILITY:stockitem.EXCISEAPPLICABILITY,
    SALESTAXCESSAPPLICABLE:stockitem.SALESTAXCESSAPPLICABLE,
    VATAPPLICABLE:stockitem.VATAPPLICABLE,
    BASEUNITS:stockitem.BASEUNITS,
    ADDITIONALUNITS:stockitem.ADDITIONALUNITS,
    COSTINGMETHOD:stockitem.COSTINGMETHOD,
    VALUATIONMETHOD:stockitem.VALUATIONMETHOD,
    BASICTARIFFTYPE:stockitem.BASICTARIFFTYPE,
    VATBASEUNIT:stockitem.VATBASEUNIT,
    ISCOSTCENTRESON:stockitem.ISCOSTCENTRESON,
    ISBATCHWISEON:stockitem.ISBATCHWISEON,
    ISPERISHABLEON:stockitem.ISPERISHABLEON,
    ISENTRYTAXAPPLICABLE:stockitem.ISENTRYTAXAPPLICABLE,
    ISCOSTTRACKINGON:stockitem.ISCOSTTRACKINGON,
    ISUPDATINGTARGETID:stockitem.ISUPDATINGTARGETID,
    ASORIGINAL:stockitem.ASORIGINAL,
    ISRATEINCLUSIVEVAT:stockitem.ISRATEINCLUSIVEVAT,
    IGNOREPHYSICALDIFFERENCE:stockitem.IGNOREPHYSICALDIFFERENCE,
    IGNORENEGATIVESTOCK:stockitem.IGNORENEGATIVESTOCK,
    REORDERPERIOD:stockitem.REORDERPERIOD,
    MINORDERPERIOD:stockitem.MINORDERPERIOD,
    REORDERASHIGHER:stockitem.REORDERASHIGHER,
    MINORDERASHIGHER:stockitem.MINORDERASHIGHER,
    ISEXCISECALCULATEONMRP:stockitem.ISEXCISECALCULATEONMRP,
    INCLUSIVETAX:stockitem.INCLUSIVETAX,
    GSTCALCSLABONMRP:stockitem.GSTCALCSLABONMRP,
    MODIFYMRPRATE:stockitem.MODIFYMRPRATE,
    ALTERID:stockitem.ALTERID,
    REORDERPERIODLENGTH:stockitem.REORDERPERIODLENGTH,
    MINORDERPERIODLENGTH:stockitem.MINORDERPERIODLENGTH,
    REORDERBASE:stockitem.REORDERBASE,
    MINIMUMORDERBASE:stockitem.MINIMUMORDERBASE,
    TREATSALESASMANUFACTURED:stockitem.TREATSALESASMANUFACTURED,
    TREATPURCHASESASCONSUMED:stockitem.TREATPURCHASESASCONSUMED,
    TREATREJECTSASSCRAP:stockitem.TREATREJECTSASSCRAP,
    HASMFGDATE:stockitem.HASMFGDATE,
    ALLOWUSEOFEXPIREDITEMS:stockitem.ALLOWUSEOFEXPIREDITEMS,
    IGNOREBATCHES:stockitem.IGNOREBATCHES,
    IGNOREGODOWNS:stockitem.IGNOREGODOWNS,
    CALCONMRP:stockitem.CALCONMRP,
    EXCLUDEJRNLFORVALUATION:stockitem.EXCLUDEJRNLFORVALUATION,
    ISMRPINCLOFTAX:stockitem.ISMRPINCLOFTAX,
    ISADDLTAXEXEMPT:stockitem.ISADDLTAXEXEMPT,
    ISSUPPLEMENTRYDUTYON:stockitem.ISSUPPLEMENTRYDUTYON,
    GVATISEXCISEAPPL:stockitem.GVATISEXCISEAPPL,
    DENOMINATOR:stockitem.DENOMINATOR,
    RATEOFVAT:stockitem.RATEOFVAT,
    VATBASENO:stockitem.VATBASENO,
    VATTRAILNO:stockitem.VATTRAILNO,
    VATACTUALRATIO:stockitem.VATACTUALRATIO,
    NATUREOFITEM:stockitem.NATUREOFITEM,
    VATCOMMODITY:stockitem.VATCOMMODITY,
    RATEOFMRP:stockitem.RATEOFMRP,
    NARRATION:stockitem.NARRATION,
    TCSCATEGORY:stockitem.TCSCATEGORY,
    PARENT:stockitem.PARENT[0],
    EXCISEITEMCLASSIFICATION:stockitem.EXCISEITEMCLASSIFICATION[0],
    DESCRIPTION:stockitem.DESCRIPTION[0],
    OPENINGBALANCE:stockitem.OPENINGBALANCE[0],
    OPENINGVALUE:stockitem.OPENINGVALUE[0],
    OPENINGRATE:stockitem.OPENINGRATE[0]

    }
    )<-[:contains]-(c)

    foreach(std in st.SERVICETAXDETAILSLIST | merge(stockitems)-[:has]->(:SERVICETAXDETAILS
    {})
    )
    foreach(scdl in st.SALESTAXCESSDETAILSLISTLIST | merge(stockitems)-[:has]->(:SALESTAXCESSDETAILS
    {})
    )
    foreach(sdl in st.SCHVIDETAILSLIST | merge(stockitems)-[:has]->(:SCHVIDETAILS
    {})
    )
    foreach(tcdl in st.TCSCATEGORYDETAILS | merge(stockitems)-[:has]->(:TCSCATEGORYDETAILS
    {})
    )
    foreach(tdcdl in st.TDSCATEGORYDETAILSLIST | merge(stockitems)-[:has]->(:TDSCATEGORYDETAILS
    {})
    )
    foreach(etl in st.EXCLUDEDTAXATIONSLIST | merge(stockitems)-[:has]->(:EXCLUDEDTAXATIONS
    {})
    )
    foreach(oael in st.OLDAUDITENTRIESLIST | merge(stockitems)-[:has]->(:OLDAUDITENTRIES
    {})
    )
    foreach(aael in st.ACCOUNTAUDITENTRIESLIST | merge(stockitems)-[:has]->(:ACCOUNTAUDITENTRIES
    {})
    )
    foreach(ael in st.AUDITENTRIESLIST | merge(stockitems)-[:has]->(:AUDITENTRIES
    {})
    )
    foreach(mdl in st.MRPDETAILSLIST | merge(stockitems)-[:has]->(:MRPDETAILS
    {})
    )
    foreach(vcdl in st.VATCLASSIFICATIONDETAILSLIST | merge(stockitems)-[:has]->(:VATCLASSIFICATIONDETAILS
    {})
    )
    foreach(cll in st.COMPONENTLISTLIST | merge(stockitems)-[:has]->(:COMPONENTLIST
    {})
    )
    foreach(aald in st.ADDITIONALLEDGERSLIST | merge(stockitems)-[:has]->(:ADDITIONALLEDGERS
    {})
    )
    foreach(tedl in st.TRADEREXCISEDUTIESLIST | merge(stockitems)-[:has]->(:TRADEREXCISEDUTIES
    {})
    )
    foreach(ldl in st.LBTDETAILSLIST | merge(stockitems)-[:has]->(:LBTDETAILS
    {})
    )
    foreach(pll in st.PRICELEVELLISTLIST | merge(stockitems)-[:has]->(:PRICELEVELLIST
    {})
    )
    foreach(gcsl in st.GSTCLASSFNIGSTRATESLIST| merge(stockitems)-[:has]->(:GSTCLASSFNIGSTRATES
    {})
    )
    foreach(etdhal in st.EXTARIFFDUTYHEADDETAILSLIST | merge(stockitems)-[:has]->(:EXTARIFFDUTYHEADDETAILS
    {})
    )
    foreach(tgll in st.TEMPGSTITEMSLABRATESLIST | merge(stockitems)-[:has]->(:TEMPGSTITEMSLABRATES
    {})
    )
    foreach(oaei in st.OLDAUDITENTRYIDSLIST | merge(stockitems)-[:has]->(:OLDAUDITENTRYIDS
    {TYPE:oaei.TYPE,
    OLDAUDITENTRYIDS:oaei.OLDAUDITENTRYIDS})
    )
    foreach(vd in st.VATDETAILS | merge(stockitems)-[:has]->(:VATDETAIL
    {FROMDATE:vd.FROMDATE,
    TAXTYPE:vd.TAXTYPE,
    ISINVDETAILSENABLE:vd.ISINVDETAILSENABLE,
    ISCALCONACTUALQTY:vd.ISCALCONACTUALQTY,
    RATEOFVAT:vd.RATEOFVAT
    })
    )
    foreach(gdl in st.GSTDETAILSLIST | merge(stockitems)-[:has]->(gstdetailslists:GSTDETAILSLISTS
    {APPLICABLEFROM:gdl.APPLICABLEFROM,
    CALCULATIONTYPE:gdl.CALCULATIONTYPE,
    HSNMASTERNAME:gdl.HSNMASTERNAME,
    TAXABILITY:gdl.TAXABILITY,
    ISREVERSECHARGEAPPLICABLE:gdl.ISREVERSECHARGEAPPLICABLE,
    ISNONGSTGOODS:gdl.ISNONGSTGOODS,
    GSTINELIGIBLEITC:gdl.GSTINELIGIBLEITC,
    INCLUDEEXPFORSLABCALC:gdl.INCLUDEEXPFORSLABCALC
    })
    foreach(swdl in gdl.STATEWISEDETAILSLIST | merge(gstdetailslists)-[:has]->(:STATEWISEDETAILSLIST
    {STATENAME:swdl.STATENAME})
    )
    foreach(glrl in gdl.GSTSLABRATESLIST | merge(gstdetailslists)-[:has]->(:GSTSLABRATESLIST
    {TAXABILITY:glrl.TAXABILITY,
    TOITEMRATE:glrl.TOITEMRATE})
    )
    )
    foreach(etdl in st.EXCISETARIFFDETAILSLIST | merge(stockitems)-[:has]->(excisetariffdetailslists:EXCISETARIFFDETAILSLISTS
    {APPLICABLEFROM:etdl.APPLICABLEFROM,
    TYPEOFTARIFF:etdl.TYPEOFTARIFF,
    REPORTINGUOM:etdl.REPORTINGUOM,
    TARIFFNAME:etdl.TARIFFNAME,
    HSNCODE:etdl.HSNCODE,
    VALUATIONTYPE:etdl.VALUATIONTYPE,
    ISEXCISECALCULATEONMRP:etdl.ISEXCISECALCULATEONMRP,
    ISNONDUTIABLE:etdl.ISNONDUTIABLE})
    foreach(edhdl in etdl.EXCISEDUTYHEADDETAILSLIST | merge(excisetariffdetailslists)-[:has]->(:EXCISEDUTYHEADDETAILSLIST
    {VALUATIONTYPE:edhdl.VALUATIONTYPE,
    DUTYHEAD:edhdl.DUTYHEAD,
    EXCISERATE:edhdl.EXCISERATE})
    )
    )
    foreach(fpl in st.FULLPRICELIST | merge(stockitems)-[:has]->(:FULLPRICE
    {DATE:fpl.DATE,
    PRICELEVEL:fpl.PRICELEVEL
    })
    )
    foreach(sl in st.SALESLIST | merge(stockitems)-[:has]->(:SALES
    {NAME:sl.NAME,
    CLASSRATE:sl.CLASSRATE,
    VATCLASSIFICATIONNATURE:sl.VATCLASSIFICATIONNATURE,
    GSTCLASSIFICATIONNATURE:sl.GSTCLASSIFICATIONNATURE,
    LEDGERFROMITEM:sl.LEDGERFROMITEM,
    REMOVEZEROENTRIES:sl.REMOVEZEROENTRIES,
    TAXCLASSIFICATIONNAME:sl.TAXCLASSIFICATIONNAME,
    ROUNDTYPE:sl.ROUNDTYPE,
    ROUNDLIMIT:sl.ROUNDLIMIT
    })
    )
    foreach(pl in st.PURCHASELIST | merge(stockitems)-[:has]->(:PURCHASES
    {NAME:pl.NAME,
    CLASSRATE:pl.CLASSRATE,
    VATCLASSIFICATIONNATURE:pl.VATCLASSIFICATIONNATURE,
    GSTCLASSIFICATIONNATURE:pl.GSTCLASSIFICATIONNATURE,
    LEDGERFROMITEM:pl.LEDGERFROMITEM,
    REMOVEZEROENTRIES:pl.REMOVEZEROENTRIES,
    TAXCLASSIFICATIONNAME:pl.TAXCLASSIFICATIONNAME,
    ROUNDTYPE:pl.ROUNDTYPE,
    ROUNDLIMIT:pl.ROUNDLIMIT
    })
    )
    foreach(bal in st.BATCHALLOCATIONSLIST | merge(stockitems)-[:has]->(:BATCHALLOCATIONS
    {GODOWNNAME:bal.GODOWNNAME,
    BATCHNAME:bal.BATCHNAME,
    MFDON:bal.MFDON,
    EXPON:bal.EXPON,
    OPENINGBALANCE:bal.OPENINGBALANCE,
    OPENINGVALUE:bal.OPENINGVALUE,
    OPENINGRATE:bal.OPENINGRATE
    })
    )
    foreach(scl in st.STANDARDCOSTLIST | merge(stockitems)-[:has]->(:STANDARDCOST
    {DATE:scl.DATE,
    RATE:scl.RATE
    })
    )
    foreach(spl in st.STANDARDPRICELIST | merge(stockitems)-[:has]->(:STANDARDPRICE
    {DATE:spl.DATE,
    RATE:spl.RATE
    })
    )
    foreach(eigl in st.EXCISEITEMGODOWNLIST | merge(stockitems)-[:has]->(exciseitemgodownlists:EXCISEITEMGODOWNLISTS
    {EXCISEALLOCTYPE:eigl.EXCISEALLOCTYPE,
    TAXUNITNAME:eigl.TAXUNITNAME,
    EXCISEGODOWNNAME:eigl.EXCISEGODOWNNAME,
    STOCKITEMTYPE:eigl.STOCKITEMTYPE,
    EXCISEREPUNITSSTR:eigl.EXCISEREPUNITSSTR,
    EXCISECONVUNIT:eigl.EXCISECONVUNIT,
    EXCISEALTREPUNITS:eigl.EXCISEALTREPUNITS,
    EXCISEREPDENOMINATOR:eigl.EXCISEREPDENOMINATOR
    })
    foreach(edl in eigl.EXCISEDUTIESLIST | merge(exciseitemgodownlists)-[:has]->(:EXCISEDUTIESLIST
    {TYPEOFDUTIES:edl.TYPEOFDUTIES,
    METHODOFCALC:edl.METHODOFCALC}))
    )

    foreach(mcl in st.MULTICOMPONENTLIST | merge(stockitems)-[:has]->(:MULTICOMPONENT
    {COMPONENTLISTNAME:mcl.COMPONENTLISTNAME,
    COMPONENTBASICQTY:mcl.COMPONENTBASICQTY
    })
    )
    )

    """
    graph.run(create_stockitem,jsonobj=content)
    return "Stock Items created successfully"

# API to create Stock Item nodes.
@app.route('/AddPBXMLStockItem',methods=['POST'])
def AddPBXMLStockItem():
    print(request.is_json)
    content = request.get_json()
    print(content)

    create_stockitem = """
    WITH {jsonobj} as v

    unwind v.PBXMLStockItems as val
    unwind val.PBXMLStockItem as st
    merge(stockitem:StockItem
    {
    NAME:st.NAME,
    GUID:st.GUID,
    CATEGORY:st.CATEGORY,
    GSTAPPLICABLE:st.GSTAPPLICABLE,
    TAXCLASSIFICATIONNAME:st.TAXCLASSIFICATIONNAME,
    GSTTYPEOFSUPPLY:st.GSTTYPEOFSUPPLY,
    EXCISEAPPLICABILITY:st.EXCISEAPPLICABILITY,
    SALESTAXCESSAPPLICABLE:st.SALESTAXCESSAPPLICABLE,
    VATAPPLICABLE:st.VATAPPLICABLE,
    BASEUNITS:st.BASEUNITS,
    ADDITIONALUNITS:st.ADDITIONALUNITS,
    COSTINGMETHOD:st.COSTINGMETHOD,
    VALUATIONMETHOD:st.VALUATIONMETHOD,
    BASICTARIFFTYPE:st.BASICTARIFFTYPE,
    VATBASEUNIT:st.VATBASEUNIT,
    ISCOSTCENTRESON:st.ISCOSTCENTRESON,
    ISBATCHWISEON:st.ISBATCHWISEON,
    ISPERISHABLEON:st.ISPERISHABLEON,
    ISENTRYTAXAPPLICABLE:st.ISENTRYTAXAPPLICABLE,
    ISCOSTTRACKINGON:st.ISCOSTTRACKINGON,
    ISUPDATINGTARGETID:st.ISUPDATINGTARGETID,
    ASORIGINAL:st.ASORIGINAL,
    ISRATEINCLUSIVEVAT:st.ISRATEINCLUSIVEVAT,
    IGNOREPHYSICALDIFFERENCE:st.IGNOREPHYSICALDIFFERENCE,
    IGNORENEGATIVESTOCK:st.IGNORENEGATIVESTOCK,
    REORDERPERIOD:st.REORDERPERIOD,
    MINORDERPERIOD:st.MINORDERPERIOD,
    REORDERASHIGHER:st.REORDERASHIGHER,
    MINORDERASHIGHER:st.MINORDERASHIGHER,
    ISEXCISECALCULATEONMRP:st.ISEXCISECALCULATEONMRP,
    INCLUSIVETAX:st.INCLUSIVETAX,
    GSTCALCSLABONMRP:st.GSTCALCSLABONMRP,
    MODIFYMRPRATE:st.MODIFYMRPRATE,
    ALTERID:st.ALTERID,
    REORDERPERIODLENGTH:st.REORDERPERIODLENGTH,
    MINORDERPERIODLENGTH:st.MINORDERPERIODLENGTH,
    REORDERBASE:st.REORDERBASE,
    MINIMUMORDERBASE:st.MINIMUMORDERBASE,
    TREATSALESASMANUFACTURED:st.TREATSALESASMANUFACTURED,
    TREATPURCHASESASCONSUMED:st.TREATPURCHASESASCONSUMED,
    TREATREJECTSASSCRAP:st.TREATREJECTSASSCRAP,
    HASMFGDATE:st.HASMFGDATE,
    ALLOWUSEOFEXPIREDITEMS:st.ALLOWUSEOFEXPIREDITEMS,
    IGNOREBATCHES:st.IGNOREBATCHES,
    IGNOREGODOWNS:st.IGNOREGODOWNS,
    CALCONMRP:st.CALCONMRP,
    EXCLUDEJRNLFORVALUATION:st.EXCLUDEJRNLFORVALUATION,
    ISMRPINCLOFTAX:st.ISMRPINCLOFTAX,
    ISADDLTAXEXEMPT:st.ISADDLTAXEXEMPT,
    ISSUPPLEMENTRYDUTYON:st.ISSUPPLEMENTRYDUTYON,
    GVATISEXCISEAPPL:st.GVATISEXCISEAPPL,
    DENOMINATOR:st.DENOMINATOR,
    RATEOFVAT:st.RATEOFVAT,
    VATBASENO:st.VATBASENO,
    VATTRAILNO:st.VATTRAILNO,
    VATACTUALRATIO:st.VATACTUALRATIO,
    NATUREOFITEM:st.NATUREOFITEM,
    VATCOMMODITY:st.VATCOMMODITY,
    RATEOFMRP:st.RATEOFMRP,
    NARRATION:st.NARRATION,
    TCSCATEGORY:st.TCSCATEGORY,
    PARENT:st.PARENT[0],
    EXCISEITEMCLASSIFICATION:st.EXCISEITEMCLASSIFICATION[0],
    DESCRIPTION:st.DESCRIPTION[0],
    OPENINGBALANCE:st.OPENINGBALANCE[0],
    OPENINGVALUE:st.OPENINGVALUE[0],
    OPENINGRATE:st.OPENINGRATE[0]

    }
    )<-[:contains]-(c)

    foreach(std in st.SERVICETAXDETAILSLIST | merge(stockitems)-[:has]->(:SERVICETAXDETAILS
    {})
    )
    foreach(scdl in st.SALESTAXCESSDETAILSLISTLIST | merge(stockitems)-[:has]->(:SALESTAXCESSDETAILS
    {})
    )
    foreach(sdl in st.SCHVIDETAILSLIST | merge(stockitems)-[:has]->(:SCHVIDETAILS
    {})
    )
    foreach(tcdl in st.TCSCATEGORYDETAILS | merge(stockitems)-[:has]->(:TCSCATEGORYDETAILS
    {})
    )
    foreach(tdcdl in st.TDSCATEGORYDETAILSLIST | merge(stockitems)-[:has]->(:TDSCATEGORYDETAILS
    {})
    )
    foreach(etl in st.EXCLUDEDTAXATIONSLIST | merge(stockitems)-[:has]->(:EXCLUDEDTAXATIONS
    {})
    )
    foreach(oael in st.OLDAUDITENTRIESLIST | merge(stockitems)-[:has]->(:OLDAUDITENTRIES
    {})
    )
    foreach(aael in st.ACCOUNTAUDITENTRIESLIST | merge(stockitems)-[:has]->(:ACCOUNTAUDITENTRIES
    {})
    )
    foreach(ael in st.AUDITENTRIESLIST | merge(stockitems)-[:has]->(:AUDITENTRIES
    {})
    )
    foreach(mdl in st.MRPDETAILSLIST | merge(stockitems)-[:has]->(:MRPDETAILS
    {})
    )
    foreach(vcdl in st.VATCLASSIFICATIONDETAILSLIST | merge(stockitems)-[:has]->(:VATCLASSIFICATIONDETAILS
    {})
    )
    foreach(cll in st.COMPONENTLISTLIST | merge(stockitems)-[:has]->(:COMPONENTLIST
    {})
    )
    foreach(aald in st.ADDITIONALLEDGERSLIST | merge(stockitems)-[:has]->(:ADDITIONALLEDGERS
    {})
    )
    foreach(tedl in st.TRADEREXCISEDUTIESLIST | merge(stockitems)-[:has]->(:TRADEREXCISEDUTIES
    {})
    )
    foreach(ldl in st.LBTDETAILSLIST | merge(stockitems)-[:has]->(:LBTDETAILS
    {})
    )
    foreach(pll in st.PRICELEVELLISTLIST | merge(stockitems)-[:has]->(:PRICELEVELLIST
    {})
    )
    foreach(gcsl in st.GSTCLASSFNIGSTRATESLIST| merge(stockitems)-[:has]->(:GSTCLASSFNIGSTRATES
    {})
    )
    foreach(etdhal in st.EXTARIFFDUTYHEADDETAILSLIST | merge(stockitems)-[:has]->(:EXTARIFFDUTYHEADDETAILS
    {})
    )
    foreach(tgll in st.TEMPGSTITEMSLABRATESLIST | merge(stockitems)-[:has]->(:TEMPGSTITEMSLABRATES
    {})
    )
    foreach(oaei in st.OLDAUDITENTRYIDSLIST | merge(stockitems)-[:has]->(:OLDAUDITENTRYIDS
    {TYPE:oaei.TYPE,
    OLDAUDITENTRYIDS:oaei.OLDAUDITENTRYIDS})
    )
    foreach(vd in st.VATDETAILS | merge(stockitems)-[:has]->(:VATDETAIL
    {FROMDATE:vd.FROMDATE,
    TAXTYPE:vd.TAXTYPE,
    ISINVDETAILSENABLE:vd.ISINVDETAILSENABLE,
    ISCALCONACTUALQTY:vd.ISCALCONACTUALQTY,
    RATEOFVAT:vd.RATEOFVAT
    })
    )
    foreach(gdl in st.GSTDETAILSLIST | merge(stockitems)-[:has]->(gstdetailslists:GSTDETAILSLISTS
    {APPLICABLEFROM:gdl.APPLICABLEFROM,
    CALCULATIONTYPE:gdl.CALCULATIONTYPE,
    HSNMASTERNAME:gdl.HSNMASTERNAME,
    TAXABILITY:gdl.TAXABILITY,
    ISREVERSECHARGEAPPLICABLE:gdl.ISREVERSECHARGEAPPLICABLE,
    ISNONGSTGOODS:gdl.ISNONGSTGOODS,
    GSTINELIGIBLEITC:gdl.GSTINELIGIBLEITC,
    INCLUDEEXPFORSLABCALC:gdl.INCLUDEEXPFORSLABCALC
    })
    foreach(swdl in gdl.STATEWISEDETAILSLIST | merge(gstdetailslists)-[:has]->(:STATEWISEDETAILSLIST
    {STATENAME:swdl.STATENAME})
    )
    foreach(glrl in gdl.GSTSLABRATESLIST | merge(gstdetailslists)-[:has]->(:GSTSLABRATESLIST
    {TAXABILITY:glrl.TAXABILITY,
    TOITEMRATE:glrl.TOITEMRATE})
    )
    )
    foreach(etdl in st.EXCISETARIFFDETAILSLIST | merge(stockitems)-[:has]->(excisetariffdetailslists:EXCISETARIFFDETAILSLISTS
    {APPLICABLEFROM:etdl.APPLICABLEFROM,
    TYPEOFTARIFF:etdl.TYPEOFTARIFF,
    REPORTINGUOM:etdl.REPORTINGUOM,
    TARIFFNAME:etdl.TARIFFNAME,
    HSNCODE:etdl.HSNCODE,
    VALUATIONTYPE:etdl.VALUATIONTYPE,
    ISEXCISECALCULATEONMRP:etdl.ISEXCISECALCULATEONMRP,
    ISNONDUTIABLE:etdl.ISNONDUTIABLE})
    foreach(edhdl in etdl.EXCISEDUTYHEADDETAILSLIST | merge(excisetariffdetailslists)-[:has]->(:EXCISEDUTYHEADDETAILSLIST
    {VALUATIONTYPE:edhdl.VALUATIONTYPE,
    DUTYHEAD:edhdl.DUTYHEAD,
    EXCISERATE:edhdl.EXCISERATE})
    )
    )
    foreach(fpl in st.FULLPRICELIST | merge(stockitems)-[:has]->(:FULLPRICE
    {DATE:fpl.DATE,
    PRICELEVEL:fpl.PRICELEVEL
    })
    )
    foreach(sl in st.SALESLIST | merge(stockitems)-[:has]->(:SALES
    {NAME:sl.NAME,
    CLASSRATE:sl.CLASSRATE,
    VATCLASSIFICATIONNATURE:sl.VATCLASSIFICATIONNATURE,
    GSTCLASSIFICATIONNATURE:sl.GSTCLASSIFICATIONNATURE,
    LEDGERFROMITEM:sl.LEDGERFROMITEM,
    REMOVEZEROENTRIES:sl.REMOVEZEROENTRIES,
    TAXCLASSIFICATIONNAME:sl.TAXCLASSIFICATIONNAME,
    ROUNDTYPE:sl.ROUNDTYPE,
    ROUNDLIMIT:sl.ROUNDLIMIT
    })
    )
    foreach(pl in st.PURCHASELIST | merge(stockitems)-[:has]->(:PURCHASES
    {NAME:pl.NAME,
    CLASSRATE:pl.CLASSRATE,
    VATCLASSIFICATIONNATURE:pl.VATCLASSIFICATIONNATURE,
    GSTCLASSIFICATIONNATURE:pl.GSTCLASSIFICATIONNATURE,
    LEDGERFROMITEM:pl.LEDGERFROMITEM,
    REMOVEZEROENTRIES:pl.REMOVEZEROENTRIES,
    TAXCLASSIFICATIONNAME:pl.TAXCLASSIFICATIONNAME,
    ROUNDTYPE:pl.ROUNDTYPE,
    ROUNDLIMIT:pl.ROUNDLIMIT
    })
    )
    foreach(bal in st.BATCHALLOCATIONSLIST | merge(stockitems)-[:has]->(:BATCHALLOCATIONS
    {GODOWNNAME:bal.GODOWNNAME,
    BATCHNAME:bal.BATCHNAME,
    MFDON:bal.MFDON,
    EXPON:bal.EXPON,
    OPENINGBALANCE:bal.OPENINGBALANCE,
    OPENINGVALUE:bal.OPENINGVALUE,
    OPENINGRATE:bal.OPENINGRATE
    })
    )
    foreach(scl in st.STANDARDCOSTLIST | merge(stockitems)-[:has]->(:STANDARDCOST
    {DATE:scl.DATE,
    RATE:scl.RATE
    })
    )
    foreach(spl in st.STANDARDPRICELIST | merge(stockitems)-[:has]->(:STANDARDPRICE
    {DATE:spl.DATE,
    RATE:spl.RATE
    })
    )
    foreach(eigl in st.EXCISEITEMGODOWNLIST | merge(stockitems)-[:has]->(exciseitemgodownlists:EXCISEITEMGODOWNLISTS
    {EXCISEALLOCTYPE:eigl.EXCISEALLOCTYPE,
    TAXUNITNAME:eigl.TAXUNITNAME,
    EXCISEGODOWNNAME:eigl.EXCISEGODOWNNAME,
    STOCKITEMTYPE:eigl.STOCKITEMTYPE,
    EXCISEREPUNITSSTR:eigl.EXCISEREPUNITSSTR,
    EXCISECONVUNIT:eigl.EXCISECONVUNIT,
    EXCISEALTREPUNITS:eigl.EXCISEALTREPUNITS,
    EXCISEREPDENOMINATOR:eigl.EXCISEREPDENOMINATOR
    })
    foreach(edl in eigl.EXCISEDUTIESLIST | merge(exciseitemgodownlists)-[:has]->(:EXCISEDUTIESLIST
    {TYPEOFDUTIES:edl.TYPEOFDUTIES,
    METHODOFCALC:edl.METHODOFCALC}))
    )

    foreach(mcl in st.MULTICOMPONENTLIST | merge(stockitems)-[:has]->(:MULTICOMPONENT
    {COMPONENTLISTNAME:mcl.COMPONENTLISTNAME,
    COMPONENTBASICQTY:mcl.COMPONENTBASICQTY
    })
    )
    

    """
    graph.run(create_stockitem,jsonobj=content)
    return "Stock Item created successfully"

@app.route('/getAllStockItems',methods=['GET'])
def getAllStockItems():

    get_all_stockitems = """
    match(stockitem:Stockitems)
    return stockitem
    """
    result = []
    for res in graph.run(get_all_stockitems):
        result.append(str(res[0]))
    return jsonify(result)

@app.route('/getStockItem',methods=['GET'])
def getStockItem():
    name = request.args['name']
    get_stockitem_details = """
    match(stockitem:Stockitems)
    where stockitem.NAME = {NAME}
    return stockitem
    """
    result = jsonify(graph.run(get_stockitem_details,NAME=name).data())
    return result

app.run(host='127.0.0.1', port=5000)