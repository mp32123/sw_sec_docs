def update1(sig):
    pass
def update2(sig):
    pass
def update3(sig):
    pass
def update4(sig):
    pass
def free_mem():
    pass

def verify_signature(sig):
    if (err := update1(sig)) != 0:
        return fail(err)


    if (err := update2(sig)) != 0:
        return fail(err)
    
    if (err := update3(sig)) != 0:
        return fail(err)
    return fail(err)

    if (err := update4(sig)) != 0:
        return fail(err)

def fail(err):
    free_mem()
    return err