def isprime(number):
    for i in range(2, number + 1):
        count = 0
        for n in range(1, i + 1):
            if i % n == 0:
                count = count + 1
            if count > 2:
                return False
        if count == 2:
            return True

def factorize(number):
    if number<1:
        raise ValueError("Value cannot be less than 1")
    elif isinstance(number,float):
        raise TypeError("Value cannot be float")
    else:
        res = []
        for z in range(2,number+1):
            x = 0
            y = 1
            if isprime(z):
                while number % y == 0:
                    x = x + 1
                    y = pow(z, x)
                y = y / z
                if (x - 1) != 0:
                    res.append((z, x - 1))
                number = number / y
            if number==1:
                break
        return res

def get_hcf(list1,list2):
    if len(list1)==0 or len(list2)==0:
        return []
    else:
        res=[]
        for set1 in list1:
            for set2 in list2:
                if set1[0]==set2[0]:
                    res.append((set1[0],min(set1[1],set2[1])))
                    continue
        return res

def get_lcm(list1,list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1==0:
        return list2
    elif len2==0:
        return list1
    else:
        res=[]
        i=0;j=0
        while i<len1 and j<len2:
            while list1[i][0]<=list2[j][0]:
                if(list1[i][0]==list2[j][0]):
                    res.append((list1[i][0],max(list1[i][1],list2[j][1])))
                    i+=1
                    j+=1
                else:
                    res.append(list1[i])
                    i+=1
                if (i >= len1):
                    res.extend(list2[j:])
                    return res
                if (j >= len2):
                    res.extend(list1[i:])
                    return
            while list2[j][0]<=list1[i][0]:
                if(list2[j][0]==list1[i][0]):
                    res.append((list2[j][0],max(list1[i][1],list2[j][1])))
                    i+=1
                    j+=1
                else:
                    res.append(list2[j])
                    j+=1
                if (i >= len1):
                    res.extend(list2[j:])
                    return res
                if (j >= len2):
                    res.extend(list1[i:])
                    return res
        return res

def multiply(list1,list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1==0:
        return list2
    elif len2==0:
        return list1
    else:
        res=[]
        i=0;j=0
        while i<len1 and j<len2:
            while list1[i][0]<=list2[j][0]:
                if(list1[i][0]==list2[j][0]):
                    res.append((list1[i][0],int(list1[i][1])+int(list2[j][1])))
                    i+=1
                    j+=1
                else:
                    res.append(list1[i])
                    i+=1
                if (i >= len1):
                    res.extend(list2[j:])
                    return res
                if (j >= len2):
                    res.extend(list1[i:])
                    return
            while list2[j][0]<=list1[i][0]:
                if(list2[j][0]==list1[i][0]):
                    res.append((list2[j][0],int(list1[i][1])+int(list2[j][1])))
                    i+=1
                    j+=1
                else:
                    res.append(list2[j])
                    j+=1
                if (i >= len1):
                    res.extend(list2[j:])
                    return res
                if (j >= len2):
                    res.extend(list1[i:])
                    return res
        return res
