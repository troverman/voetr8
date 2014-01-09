################################################################
####controllers#################################################
################################################################

################################
####about#######################
################################
def about():

    return dict()
    
################################
####account#####################
################################    
def account():

    return dict()

################################
####api#########################
################################    
def api():

    return dict()
            
################################
####committee###################
################################     
def committee():
    
    if request.args(0) is None:
        redirect(URL('committees'))

    selected_committee = db(db.committee.title==request.args(0).replace("-"," ")).select()
    selected_committee_children = db(db.committee.parent_committee_id == selected_committee[0]['id']).select()    
    statutes_by_parent = db(db.statute.parent_committee_id == selected_committee[0]['id']).select()
    
    return dict(
    
        selected_committee=selected_committee,
        selected_committee_children=selected_committee_children,
        statutes_by_parent=statutes_by_parent,
    
    )

################################
####committees##################
################################
def committees():
    
    default_parent_committee_list = db(db.committee.parent_committee_id==0).select() 
    
    return dict(
        default_parent_committee_list=default_parent_committee_list   
    )

################################
####contact#####################
################################        
def contact():

    return dict()  
    
################################
####discover####################
################################
def discover():

    return dict()
    
################################
####faq#########################
################################                        
def faq():

    return dict()

################################
####feed########################
################################                        
def feed():

    return dict()
    
################################
####index#######################
################################       
def index():

    response.flash = T("let's change the world! :)")
    return dict()

################################
####member######################
################################
def member():

    return dict()
    
################################
####mission#####################
################################        
def mission():

    return dict() 

################################
####post########################
################################        
def post():

    return dict() 
            
################################
####privacy#####################
################################        
def privacy():

    return dict() 
        
################################
####search######################
################################
def search():

    return dict()   
 
################################
####stats#######################
################################
def stats():

    return dict()  
           
################################
####terms#######################
################################        
def terms():

    return dict() 
    
################################
####thread######################
################################        
def thread():

    return dict()    
             
################################
####transparency################
################################
def transparency():

    return dict()
   
     
################################################################
####helpers#####################################################
################################################################ 

################################
####download####################
################################      
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

################################
####call########################
################################  
def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

################################
####data########################
################################  
@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
