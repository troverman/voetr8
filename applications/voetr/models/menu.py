if request.function == 'index':
    response.title = 'voetr'
else:
    response.title = request.function

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Trevor Overman'
response.meta.description = 'empowering the internet'
response.meta.keywords = 'voting, empowerment, internet'
response.meta.generator = 'Web2py Web Framework'

#members = db(db.auth_user).select()
#for member in members:
	#db.committee_member.insert(committee_id="5748256453689344", member_id=str(member['id']))
	#db.committee_member.insert(committee_id="4662445771587584", member_id=str(member['id']))

