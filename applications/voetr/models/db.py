################################################################
####db.py#######################################################
################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

################################
####database_conntection########
################################  

## connect to Google BigTable (optional 'google:datastore://namespace')
db = DAL('google:datastore')
## store sessions and tickets there
session.connect(request, response, db=db)
## or store session in Memcache, Redis, etc.
## from gluon.contrib.memdb import MEMDB
## from google.appengine.api.memcache import Client
## session.connect(request, response, db = MEMDB(Client())) 
## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

auth.define_tables(username=True, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'mail@voetr.com'
mail.settings.login = 'troverman:admin'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
db.auth_user.first_name.readable = False
db.auth_user.last_name.readable = False 

################################################################
####database_tables#############################################
################################################################

################################
####bylaw#######################
################################ 
db.define_table('bylaw',
    Field('title','string'),
    Field('content','string'),
    Field('committee_id_array','list:string'),
)

################################
####bylaw_relationship##########
################################ 
db.define_table('bylaw_relationship',
    Field('relationship_type','string'),
    Field('bylaw_id_array','list:string'),
)

################################
####bylaw_tag###################
################################ 
db.define_table('bylaw_tag',
    Field('bylaw_id','string'),
    Field('tag','string'),
)

################################
####committee###################
################################ 
db.define_table('committee',
    Field('url','string'),
    Field('title','string'),
    Field('description','string'),
)

################################
####committee_image#############
################################  
db.define_table('committee_image',
    Field('committee_id', 'string', readable=False, writable=False),
    Field('image_order','string'),
    Field('image_type','string'),
    Field('picture', 'upload', uploadfield='picture_file'),
    Field('picture_file', 'blob')
)

################################
####committee_member############
################################ 
db.define_table('committee_member',
    Field('committee_id','string'),
    Field('member_id','string'),
)

################################
####committee_tag###############
################################ 
db.define_table('committee_tag',
    Field('committee_id','string'),
    Field('tag','string'),
)

################################
####committee_member_detail#####
################################ 
db.define_table('committee_member_detail',
    Field('committee_id','string'),
    Field('member_id','string'),
    Field('detail','string'),
    Field('detail_type','string'),
)

################################
####committee_position##########
################################ 
db.define_table('committee_position',
    Field('committee_id','string'),
    Field('title','string'),
)

################################
####committee_position_detail###
################################ 
db.define_table('committee_position_detail',
    Field('committee_position_id','string'),
    Field('detail','string'),
    Field('detail_type','string'),
)

################################
####committee_relationship######
################################ 
db.define_table('committee_relationship',
    Field('relationship_type','string'),
    Field('committee_id_array','list:string'),
)

################################
####thread######################
################################ 
db.define_table('thread',
    Field('url','string'),
    Field('title','string'),
    Field('content','string'),
)

################################
####thread_tag##################
################################ 
db.define_table('thread_tag',
    Field('thread_id','string'),
    Field('tag','string'),
)
