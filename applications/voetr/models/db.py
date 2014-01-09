## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

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

## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

db.define_table('committee',
    Field('url','string'),
    Field('title','string'),
    Field('description','string'),
    Field('parent_committee_id','reference committee'),
)

db.define_table('statute',
    Field('title','string'),
    Field('description','string'),
    Field('parent_committee_id','reference committee'),
)

db.define_table('article',
    Field('title','string'),
    Field('description','string'),
    Field('parent_statute_id','reference statute'),
)

db.define_table('bylaw',
    Field('title','string'),
    Field('bylaw','string'),
    Field('parent_statute_id','reference statute'),
    Field('parent_article_id','reference article'),
)

db.define_table('bill', 
    Field('parent_committee_id','reference committee'), 
)
