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

    committee_member_array=[]
    selected_committee = db(db.committee.url == request.args(0)).select()
    selected_committee_positions = db(db.committee_position.committee_id == selected_committee[0]['id']).select()

    if request.args(1) == 'members':
        committee_members = db(db.committee_member.committee_id == selected_committee[0]['id']).select()
        for committee_member in committee_members:
            committee_member_array.append(db(db.auth_user.id == committee_member['member_id']).select()[0])

    return dict(
    
        selected_committee=selected_committee,
        selected_committee_positions=selected_committee_positions,
        committee_member_array=committee_member_array,
    
    )

################################
####committees##################
################################
def committees():
    
    committee_list = db(db.committee).select().as_list()
    import random
    random.shuffle(committee_list)
    rand_committee_list = committee_list[0:5]
    random.shuffle(committee_list)

    return dict(
        committee_list=committee_list,
        rand_committee_list=rand_committee_list, 
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

    import random
    committee_list = db(db.committee).select().as_list() 
    random.shuffle(committee_list)
    committee_list = committee_list[0:5]

    member_len = len(db(db.auth_user).select().as_list())

    response.flash = T("let's change the world! :)")
    return dict(
        committee_list=committee_list,
        member_len=member_len,
        )

################################
####logout######################
################################
def logout():
    auth.logout()
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
