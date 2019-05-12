import tableauserverclient as TSC

# create an auth object
tableau_auth = TSC.TableauAuth('ladua', 'workharder247')

# create an instance for your server
server = TSC.Server('http://tableau.sfu.ca')

# call the sign-in method with the auth object
server.auth.sign_in(tableau_auth)