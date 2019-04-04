def authoriseuser(auth,role,userrole):
    if(auth==True):
        if(role==userrole):
            return True
        else:
            return False,"Wrong User"
    else:
            return False,"Not Login"
