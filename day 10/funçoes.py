def format_name (fname,lname):
    fname.title() 
    lname.title()
    return fname + lname.title()

print(format_name("voao".title(),"vitor".title()))