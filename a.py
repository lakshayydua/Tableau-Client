import tableauserverclient as TSC

# create an auth object
tableau_auth = TSC.TableauAuth('ldua', 'workharder247', site_id='vpr')

# create an instance for your server
server = TSC.Server('https://tableau.sfu.ca')


# call the sign-in method with the auth object
request_return = server.auth.sign_in(tableau_auth)

print(request_return.)