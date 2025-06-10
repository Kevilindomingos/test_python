
def verif_email(email):
    if '@' in email and '.com' in email:
        return 'email válido'
    else:
        return 'email incorreto'
    
def test_email():
    assert verif_email('kevilin123@gmail.com') == 'email válido'
    
