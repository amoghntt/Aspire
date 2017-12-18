import testcaseread_post as p
def post(TC1,TC2):
    p.readTestCasesFromExcelFile()
    with open('/home/aspire/dev/juniper/juniper1/static/juniper/documents/opt/textrequirementprocessed.txt', 'r') as pro:
        lines= pro.readlines()
        no = 0
        i=TC1-1
        j=TC2-1
        tc1=''
        tc2=''
        for line in lines:
            if(no == i):
                print line
                tc1=line
            if(no == j):
                print line
                tc2=line
            no = no+1
    line1=tc1.split(" ")
    line2=tc2.split(" ")
    list2=[]
    for var1 in line1:
        for var2 in line2:
            if(var1==var2):
                #print var1,var2
                list2.append('')
    tc1_int= [int(s) for s in tc1.split() if s.isdigit()]
    print tc1_int
    tc2_int= [int(s) for s in tc2.split() if s.isdigit()]
    print tc2_int
    match=[]
    notmatch=[]
    length=0
    lentc1=len(tc1_int)
    lentc2=len(tc2_int)
    if(lentc1>lentc2):
        length=lentc2
    else:
        length=lentc1
    for i in range(0,length):
        if(tc1_int[i]==tc2_int[i]):
        	match.append(tc1_int[i])
        else:
            notmatch.append(tc1_int[i])
    print('matched numericals: ',match)
    print('not matched numericals: ', notmatch)
    return match,notmatch
