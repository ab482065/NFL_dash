# Football API
from espn_api.football import League
league_id = 1203846786 #your league_id
year = 2023
swid = '{BA3845EE-867D-49BC-BCA6-61BB629A20BB}' #your swid
espn_s2 = 'AEC5hln%2BPMVphKaeCzUdLZF8v9QH4qs89fOAvCbrAF1ME2xTUH9ofLZ%2BoBZEyZT6r1tld1PkW7eWHk06ja44givRw3Exc5RKJaTWE5oBgfPwkK8YEPTgiWSbm5uBs8rbLSibOcSb2uiM5F9O9oGYppZqFGxyyPhbXc56e%2BIA8o1Wu0mNP8qrrplg3R4t161DT9odsYVhKvE8hv2GNwdJPsvmnk%2FQpzyIcETvGWROwdk85%2FvpQxxshmqkdwSC5AKp4mnR%2BP8jB55oU86rKakGVRAM%2BcO0XnH7rQUAnHitjes7CQLpaXTaiqHZNjNJSlKMDKE%3D' #your espn_s2
league = League(league_id, year, espn_s2, swid)
print(league.teams[-1].__dict__)

