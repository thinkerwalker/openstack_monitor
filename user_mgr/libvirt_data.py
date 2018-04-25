import libvirt
def get_data(host,guest_name):
    conn=libvirt.open("qumu+tcp://%s/system"%(host))
    guest=conn.lookupByName(guest_name)
    print(guest.name())
